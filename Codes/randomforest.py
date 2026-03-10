import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Load Dataset
df = pd.read_csv("/accidents_main.csv")
# Drop rows where the target variable 'accident_severity' is NaN
df.dropna(subset=['accident_severity'], inplace=True)
# 2. Split Features & Target
X = df.drop("accident_severity", axis=1)
y = df["accident_severity"]
X = X.drop(columns=['accident_index'])
categorical_cols_X = X.select_dtypes(include=['object', 'category']).columns
X = pd.get_dummies(X, columns=categorical_cols_X, drop_first=True)
data_combined = pd.concat([X, y], axis=1)
data_combined.dropna(inplace=True)
X = data_combined.drop('accident_severity', axis=1)
y = data_combined['accident_severity']
# 3. Stratified Train-Test Split
X_train, X_test, y_train, y_test =
train_test_split( X, y, test_size=0.2, random_state=42, stratify=y
)
# 4. Apply SMOTE (balance classes)
sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
print("Before SMOTE:", y_train.value_counts())
print("After SMOTE:", y_train_res.value_counts())
# 5. Train RandomForest with class weights
12
model = RandomForestClassifier( n_esti
mators=300, max_depth=15, min_samples_split=4, class_weight="balanced", random_state=42
)
model.fit(X_train_res, y_train_res)
# 6. Predictions
y_pred = model.predict(X_test)
# 7. Evaluation
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
# 8. Plot Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix (Improved Model)")
plt.show(