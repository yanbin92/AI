#KNeighborsClassifierTest.py
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
x=iris.data
y=iris.target

# print(x[:2,:])
# print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

# print(y_train)

knn=KNeighborsClassifier()
knn.fit(x_train,y_train)

print(knn.predict(x_test))

print(y_test)