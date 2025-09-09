from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor,plot_tree

data = load_diabetes()
X=data.data
y=data.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = DecisionTreeRegressor(max_depth=3)
model.fit(X_train,y_train)

plot_tree(model,filled=True,feature_names=data.feature_names)
plt.show()