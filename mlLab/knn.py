from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = load_digits()
X= data.data
y=data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

ypred = model.predict(X_test)
print("Accuracy :",accuracy_score(y_test,ypred))