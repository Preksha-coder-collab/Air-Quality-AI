import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("dataset/city_day.csv")

print("Original Dataset Shape:", df.shape)

# ==========================
# REMOVE UNUSED COLUMNS
# ==========================

drop_cols = ["City", "Date", "AQI_Bucket"]

for col in drop_cols:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

# ==========================
# REMOVE Xylene
# OpenWeather API doesn't provide it
# ==========================

if "Xylene" in df.columns:
    df.drop("Xylene", axis=1, inplace=True)
    print("Removed column: Xylene")

# ==========================
# HANDLE MISSING VALUES
# ==========================

for col in df.columns:

    if df[col].dtype != "object":

        df[col] = df[col].fillna(
            df[col].median()
        )

# Remove rows where AQI missing

df = df.dropna(subset=["AQI"])

print("Cleaned Dataset Shape:", df.shape)

# ==========================
# FEATURES FOR API MODEL
# ==========================

features = [
    "PM2.5",
    "PM10",
    "NO",
    "NO2",
    "NH3",
    "CO",
    "SO2",
    "O3"
]

X = df[features]

y = df["AQI"]

print("\nFeatures Used:")
print(features)

# ==========================
# FEATURE SCALING
# ==========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# RANDOM FOREST
# ==========================

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

# ==========================
# TRAIN MODEL
# ==========================

print("\nTraining Model...")

model.fit(X_train, y_train)

# ==========================
# PREDICTIONS
# ==========================

y_pred = model.predict(X_test)

# ==========================
# EVALUATION
# ==========================

r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

print("\n===== MODEL PERFORMANCE =====")

print(
    "R2 Score :",
    round(r2, 4)
)

print(
    "MAE      :",
    round(mae, 2)
)

print(
    "RMSE     :",
    round(rmse, 2)
)

# ==========================
# SAVE MODEL
# ==========================

joblib.dump(
    model,
    "model/random_forest.pkl"
)

joblib.dump(
    scaler,
    "model/scaler.pkl"
)

print("\nModel Saved Successfully!")

print("random_forest.pkl created")

print("scaler.pkl created")