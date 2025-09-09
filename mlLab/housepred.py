import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.model_selection import train_test_split
data = {
    "Size":     [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],
    "Bedrooms": [2,    2,    3,    3,    3,    4,    4,    4,    5,    5,    5],
    "Age":      [5,    4,    3,    3,    2,    2,    1,    1,    1,    1,    1],
    "price":    [18000, 19000, 21000, 22000, 23000, 25000, 26000, 27000, 28000, 29000, 30000]
}   
df = pd.DataFrame(data)

X=df[["Size","Bedrooms","Age"]]
y=df[["price"]]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

ypred = model.predict(X_test)
print(f"r2 Score : {r2_score(y_test,ypred)}")
print(f"MAE : {mean_absolute_error(y_test,ypred)}")

plt.scatter(y_test,ypred,color ="blue")
plt.plot([y.min(),y.max()],[y.min(),y.max()],"r--")
plt.show()