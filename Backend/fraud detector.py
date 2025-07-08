# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load the Dataset
try:
    df = pd.read_csv('upi_transactions_2024.csv')
    print("✅ Dataset loaded successfully.")
    print("Columns:", df.columns.tolist())
except FileNotFoundError:
    print("❌ Error: 'upi_transactions_2024.csv' not found. Please ensure the file is in the working directory.")
    exit()

# 2. Data Preprocessing
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['transaction_hour'] = df['timestamp'].dt.hour
df['transaction_day'] = df['timestamp'].dt.dayofweek

df.fillna(df.mean(numeric_only=True), inplace=True)
df['sender_state'] = df['sender_state'].fillna(df['sender_state'].mode()[0])

label_encoder = LabelEncoder()
df['sender_age_group_encoded'] = label_encoder.fit_transform(df['sender_age_group'])
df['receiver_age_group_encoded'] = label_encoder.fit_transform(df['receiver_age_group'])

features = [
    'amount (INR)',
    'sender_age_group_encoded',
    'receiver_age_group_encoded',
    'hour_of_day',
    'is_weekend',
    'transaction_hour',
    'transaction_day'
]
X = df[features]

# 3. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train Isolation Forest Model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_scaled)

df['anomaly_score'] = model.decision_function(X_scaled)
df['is_anomaly'] = model.predict(X_scaled)
df['predicted_fraud'] = df['is_anomaly'].map({1: 0, -1: 1})

# 5. Evaluation
print("\n📊 Classification Report:")
print(classification_report(df['fraud_flag'], df['predicted_fraud'], zero_division=0))

# Confusion Matrix
cm = confusion_matrix(df['fraud_flag'], df['predicted_fraud'])
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='orange', xticklabels=['Normal', 'Fraud'], yticklabels=['Normal', 'Fraud'])
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# 6. Visualizations
plt.figure(figsize=(10, 6))
sns.countplot(data=df[df['is_anomaly'] == -1], x='sender_state', hue='predicted_fraud')
plt.title('Anomalies by Sender State')
plt.xlabel('State')
plt.ylabel('Count')
plt.legend(title='Fraud Predicted')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='is_anomaly', y='amount (INR)')
plt.title('Amount Distribution: Normal vs Anomalies')
plt.xlabel('Is Anomaly (-1 = Yes, 1 = No)')
plt.ylabel('Amount (INR)')
plt.show()

# 7. Display Only: Show Detected Fraud/Anomaly Records
print("\n🔍 Transactions Detected as Fraudulent or Anomalous:")
print(df[df['predicted_fraud'] == 1][[
    'transaction id', 'timestamp', 'amount (INR)', 'transaction_status', 'sender_state',
    'sender_bank', 'receiver_bank', 'predicted_fraud'
]].head(20))  # Showing top 20 for preview

# 8. Predict New Transactions
def predict_new_transaction(amount, sender_age_encoded, receiver_age_encoded, hour_of_day, is_weekend, transaction_hour, transaction_day):
    new_data = pd.DataFrame([[
        amount, sender_age_encoded, receiver_age_encoded, hour_of_day, is_weekend, transaction_hour, transaction_day
    ]], columns=features)

    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)
    return "Fraud" if prediction[0] == -1 else "Normal"

# Example Prediction
print("\n📌 Example Prediction for New Transaction:")
print(predict_new_transaction(15000, 2, 2, 3, 0, 3, 5))
