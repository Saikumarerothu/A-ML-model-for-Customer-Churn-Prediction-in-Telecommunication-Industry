# -*- coding: utf-8 -*-
"""MiniProject_Final_MP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A4R2hUK1VYSkQjFN61FYIpxNZq43-OyY
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
file_path = '/content/drive/MyDrive/telcom_m.csv'
df = pd.read_csv(file_path)

# Drop the 'Customer ID' column as it is not useful for prediction
df.drop(columns=['Customer ID'], inplace=True)

# Encode categorical columns
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Define features (X) and target (y)
X = df.drop(columns=['Churn Label'])
y = df['Churn Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

# Train a Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Get feature importances
feature_importances = rf.feature_importances_
features = X.columns

# Create a DataFrame for visualization
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)

# Plot the feature importances
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=importance_df)

plt.title('Feature Importances for Churn Prediction')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Confusion matrix data
confusion_matrix = np.array([[650, 19], [20, 620]])

# Labels for the axes
labels = ['Churn', 'No Churn']

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)

# Add titles and labels
plt.title('Confusion Matrix for Hidden Naive Bayes Model')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# Show the plot
plt.show()

from google.colab import drive
drive.mount('/content/drive')

"""# displaying thr importance features"""

importance_df.head(10)

data = importance_df[importance_df['Importance'] > 0.01]

data

hidden_df = df[['Contract', 'Number of Referrals']]

hidden_features =['Contract', 'Number of Referrals']

hidden_df.head()

X = df[data['Feature']]

X.head()

"""# hidden Navie bayes"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

X_train_hidden = X_train.copy()
X_train_hidden[hidden_features] = hidden_df[hidden_features]

# Initialize and train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train_hidden, y_train)

# Predict on test set
X_test_hidden = X_test.copy()
X_test_hidden[hidden_features] = hidden_df[hidden_features]

y_pred = nb_model.predict(X_test_hidden)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

print(classification_report(y_test, y_pred))