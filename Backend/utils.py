import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler


# -------------------------------
# 1. PREPROCESS DATA
# -------------------------------
def preprocess_data(df, target_col):
    df = df.copy()

    # Separate target and features
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # Fill missing values
    X = X.fillna(X.median(numeric_only=True)).fillna("missing")

    # Scaling numerical columns
    scaler = StandardScaler()
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns
    if not numeric_cols.empty:
        X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    # Encode categorical columns
    for col in X.columns:
        if X[col].dtype in ['object', 'string', 'str'] or pd.api.types.is_string_dtype(X[col]):
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))

    return X, y


# -------------------------------
# 2. TRAIN MODEL
# -------------------------------
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Upgrade to Random Forest for best balance of accuracy and fairness
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, X_test, y_test, accuracy


# -------------------------------
# 3. CALCULATE BIAS
# -------------------------------
def calculate_bias(model, X_test, y_test, sensitive_feature, original_df, target_col):
    
    # Rebuild test dataframe with original (non-encoded) values
    test_df = original_df.loc[X_test.index].copy()

    # Predictions
    test_df["prediction"] = model.predict(X_test)

    # Group-wise selection rates
    groups = test_df[sensitive_feature].unique()

    selection_rates = {}
    for group in groups:
        group_data = test_df[test_df[sensitive_feature] == group]
        selection_rate = group_data["prediction"].mean()
        selection_rates[str(group)] = float(selection_rate)

    # Disparate Impact
    min_sr = min(selection_rates.values())
    max_sr = max(selection_rates.values())

    disparate_impact = min_sr / max_sr if max_sr != 0 else 0

    return selection_rates, disparate_impact