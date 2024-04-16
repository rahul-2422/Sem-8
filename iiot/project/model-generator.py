import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load the data
data = pd.read_csv('data.csv')

# Drop the 'timestamp' column
X = data[['temperature', 'label']]
y = data['temperature']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
mse = model.score(X_test, y_test)
print(f"Mean Squared Error: {mse:.2f}")

# Save the trained model to a file
with open('linear_regression_model.pkl', 'wb') as f:
    pickle.dump(model, f)
