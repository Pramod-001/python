'''import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X= np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([10,15,20,25,30,40,50,60])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
model = LinearRegression()
model.fit(X_train,y_train)

ypred = model.predict(X_test)
yline= model.predict(X_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,yline)

plt.show()'''


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics  import mean_absolute_error,r2_score
from matplotlib import pyplot as plt
import pandas as pd

data = {
    "Size":     [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],
    "Bedrooms": [2,    2,    3,    3,    3,    4,    4,    4,    5,    5,    5],
    "Age":      [5,    4,    3,    3,    2,    2,    1,    1,    1,    1,    1],
    "price":    [18000, 19000, 21000, 22000, 23000, 25000, 26000, 27000, 28000, 29000, 30000]
}   
df = pd.DataFrame(data)

X=df[["Size","Bedrooms","Age"]]
y=df[["price"]]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
model = LinearRegression
model.fit(X_train,y_train)

ypred = model.predict(X_test)
yline = model.predict(X_train)

plt.scatter(y_test,ypred)
print("MAE : ",mean_absolute_error(y_test,ypred))
plt.plot([y.min(),y.max()],[y.min(),y.max()])

plt.show()