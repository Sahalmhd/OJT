import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# data
height =np.array ([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,65,63,68,72])\

# create a linear regression model for the dataset
model = LinearRegression()

#fit the model with appropriate data
model.fit(height,weight)

predicted_weight = model.predict(height)

print(f"intercept: {model.intercept_}")
print(f"coeffiecents:{model.coef_[0]}")

# create a  sctterplot for the above 
plt.scatter(height,weight,color="red")
plt.plot(height,predicted_weight,color="blue")
plt.xlabel("height")
plt.ylabel("weight")
plt.title("Linear Regression")
plt.show()