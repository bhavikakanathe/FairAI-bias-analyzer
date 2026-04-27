import streamlit as st
import pandas as pd
from utils import preprocess_data, train_model, calculate_bias
from gemini import get_bias_explanation, get_mitigation_analysis
import os

st.set_page_config(page_title="FairAI Bias Detection", page_icon="⚖️", layout="wide")

st.title("⚖️ FairAI: Bias Detection & Explainability Tool")
st.markdown("A working prototype for detecting tabular ML model bias and explaining it via Google Gemini.")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview", df.head())
        
        cols = df.columns.tolist()
        
        col1, col2 = st.columns(2)
        with col1:
            target_col = st.selectbox("Select Target Column (What you want to predict)", cols, index=len(cols)-1)
        with col2:
            sensitive_col = st.selectbox("Select Sensitive Attribute (e.g., Gender, Race)", [c for c in cols if c != target_col])
            
        if st.button("Run Analysis", type="primary"):
            with st.spinner("Processing data, training model, and calculating bias metrics..."):
                # ── Before Mitigation (Original Pipeline) ──
                original_df = df.copy()
                X, y = preprocess_data(df, target_col)
                model, X_test, y_test, accuracy = train_model(X, y)
                selection_rates, disparate_impact = calculate_bias(model, X_test, y_test, sensitive_col, original_df, target_col)
                
            st.header("📊 Results: Original Model")
            col_m1, col_m2 = st.columns([1, 2])
            with col_m1:
                st.metric("Model Accuracy", f"{accuracy*100:.2f}%")
                st.metric("Disparate Impact", f"{disparate_impact:.3f}", 
                          help="Ratio of lowest to highest selection rate. < 0.8 is typical evidence of potential bias.")
            with col_m2:
                st.write("**Selection Rates per Group:**")
                rates_df = pd.DataFrame(list(selection_rates.items()), columns=['Group', 'Selection Rate'])
                rates_df['Selection Rate formatted'] = rates_df['Selection Rate'].apply(lambda x: f"{x*100:.1f}%")
                st.dataframe(rates_df[['Group', 'Selection Rate formatted']], use_container_width=True, hide_index=True)
                
            st.header("🤖 Gemini Bias Explanation")
            with st.spinner("Asking Gemini for an explanation..."):
                explanation = get_bias_explanation(selection_rates, disparate_impact, sensitive_col, target_col)
                st.info(explanation)
                
            st.header("🛠️ Mitigation Application")
            st.write(f"Applying mitigation: Removing the `{sensitive_col}` feature from the dataset.")
            with st.spinner("Retraining model without sensitive feature..."):
                # ── After Mitigation Pipeline ──
                df_mitigated = df.copy()
                if sensitive_col in df_mitigated.columns:
                    df_mitigated = df_mitigated.drop(columns=[sensitive_col])

                X_mitigated, y_mitigated = preprocess_data(df_mitigated, target_col)
                model_mit, X_test_mit, y_test_mit, ack_mit = train_model(X_mitigated, y_mitigated)
                
                rates_mit, di_mit = calculate_bias(model_mit, X_test_mit, y_test_mit, sensitive_col, original_df, target_col)
                
            st.write("### Results: After Removing Sensitive Feature")
            col_after1, col_after2 = st.columns([1, 2])
            with col_after1:
                acc_diff = ack_mit - accuracy
                di_diff = di_mit - disparate_impact
                st.metric("Model Accuracy", f"{ack_mit*100:.2f}%", delta=f"{acc_diff*100:.2f}%")
                st.metric("Disparate Impact", f"{di_mit:.3f}", delta=f"{di_diff:.3f}")
            with col_after2:
                st.write("**Selection Rates per Group (Mitigated):**")
                rates_mit_df = pd.DataFrame(list(rates_mit.items()), columns=['Group', 'Selection Rate'])
                rates_mit_df['Selection Rate formatted'] = rates_mit_df['Selection Rate'].apply(lambda x: f"{x*100:.1f}%")
                st.dataframe(rates_mit_df[['Group', 'Selection Rate formatted']], use_container_width=True, hide_index=True)
                
            st.header("🤖 Gemini Evaluation of Mitigation")
            with st.spinner("Asking Gemini to evaluate the improvement..."):
                evaluation = get_mitigation_analysis(
                    selection_rates, rates_mit, disparate_impact, di_mit, sensitive_col
                )
                st.info(evaluation)
                
    except Exception as e:
        st.error(f"An error occurred: {e}")
