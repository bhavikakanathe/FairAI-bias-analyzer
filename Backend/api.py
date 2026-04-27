from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from utils import preprocess_data, train_model, calculate_bias
from gemini import get_bias_explanation, get_mitigation_analysis

app = FastAPI(title="FairAI Bias Detection API")

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "FairAI Backend Running", "version": "2.0"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    target: str = Form(...),
    sensitive: str = Form(...)
):
    try:
        # Read CSV
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Basic validation
        if target not in df.columns:
            return {"error": f"Target column '{target}' not found in dataset."}
        if sensitive not in df.columns:
            return {"error": f"Sensitive column '{sensitive}' not found in dataset."}

        # Store original for bias calculation (needs non-encoded sensitive col)
        original_df = df.copy()

        # Preprocess and train
        X, y = preprocess_data(df, target)
        model, X_test, y_test, accuracy = train_model(X, y)

        # Calculate bias
        selection_rates, disparate_impact = calculate_bias(
            model, X_test, y_test, sensitive, original_df, target
        )

        # Get Gemini explanation
        gemini_text = get_bias_explanation(
            selection_rates=selection_rates,
            disparate_impact=disparate_impact,
            sensitive_col=sensitive,
            target_col=target
        )

        return {
            "selection_rates": selection_rates,
            "disparate_impact": round(float(disparate_impact), 3),
            "accuracy": round(float(accuracy), 4),
            "affected_group": min(selection_rates, key=selection_rates.get),
            "favored_group": max(selection_rates, key=selection_rates.get),
            "gemini_explanation": gemini_text,
            "dataset_rows": len(df),
            "columns": df.columns.tolist()
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/mitigate")
async def mitigate(
    file: UploadFile = File(...),
    target: str = Form(...),
    sensitive: str = Form(...)
):
    try:
        # Read CSV
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        if target not in df.columns or sensitive not in df.columns:
            return {"error": "Invalid column names"}

        original_df = df.copy()

        # --- ORIGINAL MODEL ---
        X_orig, y_orig = preprocess_data(df.copy(), target)
        model_orig, X_test_orig, y_test_orig, acc_orig = train_model(X_orig, y_orig)
        rates_orig, di_orig = calculate_bias(
            model_orig, X_test_orig, y_test_orig, sensitive, original_df, target
        )

        # --- MITIGATED MODEL (remove sensitive column) ---
        df_mitigated = df.copy()
        if sensitive in df_mitigated.columns:
            df_mitigated = df_mitigated.drop(columns=[sensitive])

        X_mit, y_mit = preprocess_data(df_mitigated, target)
        model_mit, X_test_mit, y_test_mit, acc_mit = train_model(X_mit, y_mit)

        # For bias calc, use original df (has sensitive col) aligned to mitigated test indices
        rates_mit, di_mit = calculate_bias(
            model_mit, X_test_mit, y_test_mit, sensitive, original_df, target
        )

        # Gemini evaluation of mitigation
        gemini_text = get_mitigation_analysis(
            original_rates=rates_orig,
            mitigated_rates=rates_mit,
            original_di=di_orig,
            mitigated_di=di_mit,
            sensitive_col=sensitive
        )

        return {
            "original": {
                "selection_rates": rates_orig,
                "disparate_impact": round(float(di_orig), 3),
                "accuracy": round(float(acc_orig), 4),
            },
            "mitigated": {
                "selection_rates": rates_mit,
                "disparate_impact": round(float(di_mit), 3),
                "accuracy": round(float(acc_mit), 4),
            },
            "improvement": round(float(di_mit - di_orig), 3),
            "accuracy_change": round(float(acc_mit - acc_orig), 4),
            "gemini_evaluation": gemini_text
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/columns")
async def get_columns(file: UploadFile = File(...)):
    """Return column names from an uploaded CSV."""
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        return {
            "columns": df.columns.tolist(),
            "rows": len(df),
            "preview": df.head(3).to_dict(orient="records")
        }
    except Exception as e:
        return {"error": str(e)}