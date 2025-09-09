import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X= np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([10,15,20,25,30,40,50,60])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)

ypred = model.predict(X_test)
plt.scatter(X_train,y_train,color='blue')
yline = model.predict(X_train)
plt.plot(X_train,yline,color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()