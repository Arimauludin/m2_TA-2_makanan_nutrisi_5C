import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load Dataset
df = pd.read_csv("Food_Nutrition_Dataset.csv")

# 2. Fitur (X) dan Target (y)
X = df[['carbs']]
y = df['calories']

# 3. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Latih Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluasi Model
y_pred = model.predict(X_test)
r2 = metrics.r2_score(y_test, y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print("=== Hasil Evaluasi Model Nutrisi ===")
print(f"Intercept (B0) : {model.intercept_:.4f}")
print(f"Slope (B1)     : {model.coef_[0]:.4f}")
print(f"R-squared (R2) : {r2:.4f}")
print(f"RMSE           : {rmse:.4f}")

# 6. Simpan Model ke folder model/
joblib.dump(model, "model/model_nutrisi.pkl")
print("\n[SUCCESS] Model berhasil disimpan ke 'model/model_nutrisi.pkl'")