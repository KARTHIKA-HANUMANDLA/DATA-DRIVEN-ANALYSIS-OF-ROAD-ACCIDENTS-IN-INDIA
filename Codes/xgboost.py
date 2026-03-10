import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
# 1. Load dataset
df = pd.read_csv("/accidents_main.csv")
14
df.dropna(subset=['accident_severity'], inplace=True)
# 2. Split features & target
X = df.drop("accident_severity", axis=1)
y = df["accident_severity"]
y = y - 1
X = X.drop(columns=['accident_index'])
categorical_cols_X = X.select_dtypes(include=['object', 'category']).columns
X = pd.get_dummies(X, columns=categorical_cols_X, drop_first=True)
data_combined = pd.concat([X, y], axis=1)
data_combined.dropna(inplace=True)
X = data_combined.drop('accident_severity', axis=1)
y = data_combined['accident_severity']
# 3. Stratified train-test split
X_train, X_test, y_train, y_test =
train_test_split( X, y, test_size=0.2, stratify=y, random_state=42
)
# 4. Apply SMOTE (fix class imbalance)
sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
print("Before SMOTE:\n", y_train.value_counts())
print("\nAfter SMOTE:\n", y_train_res.value_counts())
# 5. Build XGBoost model
model = XGBClassifier( objective=' multi:softmax', num_class=3, learning_rate=0.05, n_estimators=500, max_depth=8, subsample=0.8, colsample_bytree=0.8, eval_metric='mlogloss', random_state=42
)
# Train the model
15
model.fit(X_train_res, y_train_res)
# 6. Predictions
y_pred = model.predict(X_test)
# 7. Evaluation
print("\nCONFUSION MATRIX:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))
# 8. Plot confusion matrix
plt.figure(figsize=(7,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("XGBoost Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show(