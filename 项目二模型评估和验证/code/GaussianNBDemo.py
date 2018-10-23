# GaussianNBDemo.py
import numpy as np
#te zheng
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
#biao qian  label
Y = np.array([1, 1, 1, 2, 2, 2])
# from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
print(clf.fit(X,Y))

print(clf.predict([[-0.8,-0.1]]))
