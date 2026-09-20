import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Load dataset
data = pd.read_csv("sales_data.csv")

# Step 2: Convert Date columnpython 
data['Date'] = pd.to_datetime(data['Date'])

# Step 3: Create numeric column (Day)
data['Day'] = np.arange(len(data))

# Step 4: Define X and y
X = data[['Day']]
y = data['Sales']

# Step 5: Train model
model = LinearRegression()
model.fit(X, y)

# Step 6: Predict future (next 5 days)
future_days = np.arange(len(data), len(data)+5).reshape(-1, 1)
predictions = model.predict(future_days)

# Step 7: Print predictions
print("Future Sales Predictions:")
for i, val in enumerate(predictions, 1):
    print(f"Day {len(data)+i}: {round(val, 2)}")

# Step 8: Plot graph
plt.scatter(data['Day'], y, label="Actual Data")
plt.plot(data['Day'], model.predict(X), color='red', label="Regression Line")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Prediction")
plt.legend()
plt.show()