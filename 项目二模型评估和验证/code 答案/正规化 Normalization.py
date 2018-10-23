# 正规化 Normalization.py
# 数据标准化 
from sklearn import preprocessing #标准化数据模块
import numpy as np

# 将资料分割成train与test的模块
from sklearn.model_selection import train_test_split
# 生成适合做classification资料的模块
from sklearn.datasets.samples_generator import make_classification
# Support Vector Machine中的Support Vector Classifier
from sklearn.svm import SVC
# 可视化数据的模块
import matplotlib.pyplot as plt 

# #建立Array
# a = np.array([[10, 2.7, 3.6],
#               [-100, 5, -2],
#               [120, 20, 40]], dtype=np.float64)

# #将normalized后的a打印出
# print(preprocessing.scale(a))
x,y=make_classification(
	n_samples=300,
	 n_features=2, 
	 n_redundant=0,
	 n_informative=2, 
    random_state=22, n_clusters_per_class=1, 
    scale=100
	)

# x=preprocessing.scale(x)  0.9   0.5

x_train,x_test,y_train,y_test=train_test_split(
x,y,test_size=0.3
	)

model=SVC()
model.fit(x_train,y_train)

print(model.score(x_test,y_test))
# plt.scatter(x[:,0],x[:,1],c=y)
# plt.show()
#标准化后的预测准确率提升至0.9

