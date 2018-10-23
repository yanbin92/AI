#sklearn 常用属性与功能

from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target
model = LinearRegression()
model.fit(data_X, data_y)


# print(model.predict(data_X[:4, :]))
# print(data_y[:4])

#然后，model.coef_ 和 model.intercept_ 属于 Model 的属性， 例如对于 LinearRegressor 这个模型，
#这两个属性分别输出模型的斜率和截距（与y轴的交点）。

# print(model.coef_)
# print(model.intercept_)
# print(model.get_params())

print(model.score(data_y,data_y))