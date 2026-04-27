# FairAI Bias Analyzer: Project Overview & Presentation Materials

This document contains all the necessary details about the FairAI project to help you build your PowerPoint presentation (PPT) and record your demo video.

---

## 1. The Core Problem Statement
*Why did we build this?*
- **The Issue:** AI models are increasingly used in critical decision-making (hiring, loans, healthcare). However, if these models are trained on historical data, they often inherit and amplify human biases.
- **The Gap:** Traditional data science metrics focus entirely on *accuracy* but ignore *fairness*. 
- **The Consequence:** This leads to models that may be 90% accurate but systematically reject specific demographic groups (e.g., gender, race), resulting in unfair outcomes and regulatory compliance issues.

## 2. The Solution: FairAI
*What is it?*
FairAI is an end-to-end AI governance and bias auditing platform. It allows data scientists and compliance officers to upload datasets, train machine learning models, and automatically audit them for demographic bias before they are deployed. 

**Key Value Propositions:**
1. **Automated Auditing:** Instantly calculates the *Disparate Impact Score* (the industry standard for measuring fairness).
2. **Explainability:** Uses Google Gemini to translate complex statistical disparities into a plain-English "Bias Audit Report" that non-technical stakeholders can understand.
3. **Actionable Mitigation:** Allows users to simulate fairness interventions (like removing the sensitive attribute) to see how it improves the model's fairness.

---

## 3. Technology Stack
- **Frontend / UI:** Pure HTML, JavaScript, and Tailwind CSS (Ethos Modern Design System). Fully responsive and deployed on Vercel.
- **Backend / API:** Python, FastAPI (for high-performance routing). Deployed on Render.
- **Machine Learning Engine:** Scikit-Learn (Logistic Regression) and Pandas (data processing).
- **Generative AI:** Google Gemini API (`gemini-2.0-flash`) for generating natural language explanations of bias metrics.

---

## 4. How the Application Works (The Workflow)
*Use this structure for your PPT slides.*

1. **Dashboard & Upload (Data Ingestion)**
   - The user uploads a historical dataset (e.g., a CSV of loan applications).
   - The system dynamically extracts the column names.
   - The user defines the **Target Variable** (e.g., "approved") and the **Sensitive Attribute** (e.g., "gender" or "race").
2. **Bias Analysis (The Math)**
   - The backend trains a baseline machine learning model.
   - It calculates the **Selection Rate** for each group (e.g., 80% of males approved vs 40% of females).
   - It calculates the **Disparate Impact Score**. *(Note: A score below 0.8 violates the "80% rule" used by agencies like the EEOC).*
3. **AI Decision Summary (The Magic)**
   - The statistical metrics are fed into a specialized prompt for Google Gemini.
   - Gemini acts as an "AI Fairness Auditor", returning a structured report detailing the severity of the bias, who is affected, and why it matters.
4. **Mitigation Simulation (The Fix)**
   - The system simulates a mitigation strategy (e.g., dropping the biased column or re-weighting the data).
   - It shows a side-by-side comparison of the Original Disparate Impact vs. the Projected Disparate Impact, proving the model can be made fair.

---

## 5. Demo Video Script (2-3 Minutes)

**[Scene 1: Introduction - Show the Dashboard]**
*"Hello everyone, this is FairAI. As AI takes over critical decisions in hiring and finance, ensuring these systems are fair is more important than ever. FairAI is a platform designed to detect, explain, and mitigate bias in machine learning models."*

**[Scene 2: Upload Page]**
*"Let's walk through a real-world scenario. I'm uploading a dataset of loan approvals. I'll tell the system that our target outcome is the 'approved' column, and our sensitive demographic attribute is 'gender'."*

**[Scene 3: Click Analyze & Show Analysis Page]**
*"When I click analyze, our backend trains a machine learning model on this data and immediately audits it for fairness. As you can see on the dashboard, the model achieves high accuracy, but we have a severe problem: the Disparate Impact score is below the legal threshold of 0.8. This means the model is heavily biased."*

**[Scene 4: Show AI Decision Summary Page]**
*"Numbers alone don't tell the whole story, so we integrated Google Gemini to act as an AI Fairness Auditor. Gemini takes the raw statistical metrics and generates this plain-English Bias Audit Report. It clearly explains that the female demographic is negatively impacted and provides immediate recommendations for data scientists to fix the issue."*

**[Scene 5: Show Mitigation Page]**
*"Finally, FairAI doesn't just point out problems; it helps solve them. On our Mitigation Simulation page, we can apply an algorithmic fairness constraint and immediately see the projected Disparate Impact score rise back into the safe zone."*

**[Scene 6: Outro]**
*"With FairAI, companies can ensure their AI models are accurate, transparent, and equitable before they ever reach production. Thank you."*

---

## 6. Key Selling Points (For Q&A)
- **Why Gemini?** Statistical bias metrics (like Equal Opportunity Difference) are incredibly hard for executives to understand. Gemini bridges the gap between data science and business compliance.
- **Is it scalable?** Yes, the FastAPI backend can handle massive datasets, and the decoupled architecture means the frontend can be embedded into any existing enterprise workflow.
