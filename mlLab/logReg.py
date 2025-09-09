from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_iris()
X=data.data
y=data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)
ypred=model.predict(X_test)
print("Accuracy : ",accuracy_score(y_test,ypred))
print("\nConfusion Maatrix : \n",confusion_matrix(y_test,ypred))
print("Classification : \n",classification_report(y_test,ypred))

