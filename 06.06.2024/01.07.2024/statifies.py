import pandas as pd
import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load the dataset
df = pd.read_csv('housing_price.csv')

# Define the features and target variable
x = df[['size', 'bedrooms']].values
y = df[['price']].values

# Initialize the model
model = LinearRegression()

# Define the cross-validation
loo = LeaveOneOut()

mae_scores = []

# Cross-validation loop
for train_index, test_index in loo.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Fit the model
    model.fit(x_train, y_train)
    
    # Predict the target variable
    y_pred = model.predict(x_test)
    
    # Calculate the mean absolute error
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

# Calculate the average mean absolute error
average_mae = np.mean(mae_scores)
print(f'Average mean absolute error: {average_mae}')
