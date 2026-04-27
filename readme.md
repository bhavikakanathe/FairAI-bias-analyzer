# FairAI: Bias Detection & Explainability Tool

A complete working prototype for an AI fairness auditing system built with Streamlit and Google Gemini.
It handles user uploads, trains a Logistic Regression model, calculates Selection Rates and Disparate Impact, and uses Gemini to explain the bias in plain English.

## Features
- Upload dataset and choose Target & Sensitive columns
- Automatically preprocesses the dataset
- Trains a baseline Logistic Regression model
- Calculates fairness metrics (Selection Rate and Disparate Impact)
- Explains findings via Google Gemini
- Retrains model by dropping the sensitive feature to demonstrate bias mitigation

## Local Setup Instructions

1. Ensure you have Python 3.9+ installed.
2. Navigate to this directory in your terminal.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your API key:
   - Copy `.env.example` to `.env`: `cp .env.example .env`
   - Edit `.env` and assign your Gemini key to `GEMINI_API_KEY`
5. Run the app locally:
   ```bash
   streamlit run app.py
   ```
6. Visit `http://localhost:8501` to use the application. You can upload `sample_dataset.csv` to try it out!

## Deployment Instructions (Streamlit Community Cloud)

1. Push this folder to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in.
3. Click **New app**.
4. Select your repository, branch, and set the main file path to `app.py`.
5. Under **Advanced settings**, add your `GEMINI_API_KEY` to the Secrets section:
   ```toml
   GEMINI_API_KEY="your-actual-api-key-here"
   ```
6. Click **Deploy**. In less than a minute, your app will be publicly accessible.
