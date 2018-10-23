# learn_curvetest.py
#新的模块sklearn.model_selection，将以前的sklearn.cross_validation, sklearn.grid_search 和 sklearn.learning_curve模块组合到一起
from sklearn.model_selection import learning_curve #学习曲线模块
from sklearn.datasets import load_digits
from sklearn.svm import SVC #Support Vector Classifier
import matplotlib.pyplot as plt #可视化模块
import numpy as np

data=load_digits()
X=data.data
y=data.target

#观察样本由小到大的学习曲线变化, 采用K折交叉验证 
#cv=10, 选择平均方差检视模型效能 
#scoring='mean_squared_error', 
#样本由小到大分成5轮检视学习曲线(10%, 25%, 50%, 75%, 100%):

train_sizes, train_loss, test_loss = learning_curve(
    SVC(gamma=0.001), X, y, cv=10, scoring='neg_mean_squared_error',
    train_sizes=[0.1, 0.25, 0.5, 0.75, 1])

#平均每一轮所得到的平均方差(共5轮，分别为样本10%、25%、50%、75%、100%)
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

#可视化图形:

plt.plot(train_sizes, train_loss_mean, 'o-', color="r",
         label="Training")
plt.plot(train_sizes, test_loss_mean, 'o-', color="g",
        label="Cross-validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()