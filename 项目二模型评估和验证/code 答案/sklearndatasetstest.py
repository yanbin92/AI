#sklearndatasetstest.py
# 强大数据库
from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# loaded_data = datasets.load_boston()
# data_X = loaded_data.data
# data_y = loaded_data.target
# model = LinearRegression()
# model.fit(data_X, data_y)
# print(model.predict(data_X[:4, :]))
# print(data_y[:4])

#noise 越大的话，点就会越来越离散，例如 noise 由 10 变为 50.

x,y=datasets.make_regression(
	n_samples=100,
	 n_features=1, 
	 n_informative=10, 
	 n_targets=1, bias=0.0,
	  effective_rank=None, 
	  tail_strength=0.5, 
	  noise=10.0, 
	  shuffle=True, 
	  coef=False,
	  random_state=None)

plt.scatter(x,y)
plt.show()