import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

_api_key = os.getenv("GEMINI_API_KEY")
if not _api_key:
    raise EnvironmentError("GEMINI_API_KEY is not set. Add it to your .env file.")

_client = genai.Client(api_key=_api_key)


def _format_rates(rates: dict) -> str:
    return "\n".join(
        f"  - {group}: {rate * 100:.1f}% selection rate"
        for group, rate in rates.items()
    )


def get_bias_explanation(
    selection_rates: dict,
    disparate_impact: float,
    sensitive_col: str,
    target_col: str,
) -> str:
    if not selection_rates:
        return "Cannot generate explanation: selection_rates is empty."
    
    rates_text     = _format_rates(selection_rates)
    affected_group = min(selection_rates, key=selection_rates.get)
    favored_group  = max(selection_rates, key=selection_rates.get)
    bias_level     = (
        "SEVERE"   if disparate_impact < 0.6 else
        "MODERATE" if disparate_impact < 0.8 else
        "LOW"
    )

    prompt = (
        "You are an expert AI Fairness Auditor powered by Google Gemini.\n"
        "You have just analyzed a machine learning dataset for bias.\n\n"
        "--- AUDIT RESULTS ---\n"
        f"Target Column: {target_col}\n"
        f"Sensitive Attribute: {sensitive_col}\n\n"
        f"Group Selection Rates:\n{rates_text}\n\n"
        f"Disparate Impact Score: {disparate_impact:.3f}\n"
        f"Bias Level: {bias_level}\n"
        f"Most Affected Group: {affected_group}\n"
        f"Favored Group: {favored_group}\n"
        "--- END RESULTS ---\n\n"
        "Write a bias audit report with these sections:\n"
        "## Bias Detection Summary\n"
        "## What the Numbers Mean\n"
        "## Who Is Affected and How\n"
        "## Why This Bias Likely Exists\n"
        "## Recommended Mitigations (exactly 3, with Easy/Medium/Hard ratings)\n"
        "Keep tone professional and avoid jargon."
    )

    last_error = "No models attempted"
    # Try the most likely models in order of stability (Updated based on your key's permissions)
    for model_name in ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash", "gemini-flash-latest"]:
        try:
            response = _client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            last_error = str(e)
            print(f"DEBUG: Model {model_name} failed. Error: {last_error}")
            continue

    return f"Gemini API Error: {last_error} (Last tried: {model_name})"


def get_mitigation_analysis(
    original_rates: dict,
    mitigated_rates: dict,
    original_di: float,
    mitigated_di: float,
    sensitive_col: str,
) -> str:
    if not original_rates or not mitigated_rates:
        return "Cannot generate analysis: one or both rate dictionaries are empty."

    original_rates_text  = _format_rates(original_rates)
    mitigated_rates_text = _format_rates(mitigated_rates)

    prompt = (
        "You are an AI Fairness Auditor. A bias mitigation strategy has been applied.\n\n"
        f"BEFORE Mitigation:\n"
        f"  Disparate Impact: {original_di:.3f}\n"
        f"  Selection Rates:\n{original_rates_text}\n\n"
        f"AFTER Mitigation (sensitive feature removed):\n"
        f"  Disparate Impact: {mitigated_di:.3f}\n"
        f"  Selection Rates:\n{mitigated_rates_text}\n\n"
        f"Improvement: {(mitigated_di - original_di) * 100:+.1f} percentage points\n\n"
        "Write a 3-paragraph evaluation:\n"
        "1. Did the mitigation work? By how much?\n"
        f"2. Trade-offs of removing '{sensitive_col}' from the model?\n"
        "3. What should be the next step?\n"
        "Be direct, use numbers, keep under 150 words."
    )

    last_error = "No models attempted"
    for model_name in ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-1.5-flash", "gemini-flash-latest"]:
        try:
            response = _client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            last_error = str(e)
            print(f"DEBUG: Model {model_name} failed. Error: {last_error}")
            continue

    return f"Gemini API Error: {last_error} (Last tried: {model_name})"