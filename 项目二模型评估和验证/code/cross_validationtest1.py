#cross_validationtest1.py
from sklearn.datasets import load_iris # iris数据集
from sklearn.model_selection import train_test_split # 分割数据模块
from sklearn.neighbors import KNeighborsClassifier # K最近邻(kNN，k-NearestNeighbor)分类算法
import numpy as np
#加载iris数据集
iris = load_iris()
X = iris.data
y = iris.target

#分割数据并
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

knn=KNeighborsClassifier()

#训练模型
knn.fit(X_train, y_train)

#将准确率打印出
print(knn.score(X_test, y_test))

#比如：cross_validation模块弃用，所有的包和方法都在model_selection中,包和方法名没有发生变化

from sklearn.model_selection import cross_val_score # K折交叉验证模块

#使用K折交叉验证模块
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
#将5次的预测准确率打印出
print(scores)
# [ 0.96666667  1.          0.93333333  0.96666667  1.        ]
#将5次的预测准确平均率打印出
print(scores.mean())

#以准确率(accuracy)判断 ¶
import matplotlib.pyplot as plt #可视化模块
k_range=range(1,31)

k_score=[]

for k in k_range:
	knn=KNeighborsClassifier(n_neighbors=k)
	# 以准确率(accuracy)判断 ¶
	# scores=cross_val_score(knn,X,y,cv=10,scoring='accuracy')
	#scoring params:http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
	# 以平均方差(Mean squared error) ¶ 一般来说平均方差(Mean squared error)会用于判断回归(Regression)模型的好坏。
	loss = -cross_val_score(knn, X, y, cv=10, scoring='neg_mean_squared_error')
	# k_score.append(scores.mean())
	k_score.append(loss.mean())
# print(k_range)
# print(k_score)
plt.plot(k_range,k_score)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()

#从图中可以得知，选择12~18的k值最好。高过18之后，准确率开始下降则是因为过拟合(Over fitting)的问题。

