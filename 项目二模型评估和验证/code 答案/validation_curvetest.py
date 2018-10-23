# validation_curvetest.py
# 机器学习中验证是有多么的重要, 这一次的 sklearn 中我们用到了sklearn.learning_curve当中的另外一种, 叫做validation_curve,用这一种曲线我们就能更加直观看出改变模型中的参数的时候有没有过拟合(overfitting)的问题了. 这也是可以让我们更好的选择参数的方法.
# learn_curvetest.py
#新的模块sklearn.model_selection，将以前的sklearn.cross_validation, sklearn.grid_search 和 sklearn.learning_curve模块组合到一起
from sklearn.model_selection import validation_curve #学习曲线模块
from sklearn.datasets import load_digits
from sklearn.svm import SVC #Support Vector Classifier
import matplotlib.pyplot as plt #可视化模块
import numpy as np

data=load_digits()
X=data.data
y=data.target


#建立参数测试集
param_range = np.logspace(-6, -2.3, 5)

train_loss, test_loss = validation_curve(
    SVC(), X, y, param_name='gamma', param_range=param_range, cv=10,
    scoring='neg_mean_squared_error'
    )

#平均每一轮所得到的平均方差(共5轮，分别为样本10%、25%、50%、75%、100%)
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

#可视化图形:

plt.plot(param_range, train_loss_mean, 'o-', color="r",
         label="Training")
plt.plot(param_range, test_loss_mean, 'o-', color="g",
        label="Cross-validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()

#由图中可以明显看到gamma值大于0.001，模型就会有过拟合(Overfitting)的问题。

