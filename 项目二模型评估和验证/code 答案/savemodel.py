# savemodel.py
#总算到了最后一次的课程了,我们训练好了一个Model 以后总需要保存和再次预测, 所以保存和读取我们的sklearn model也是同样重要的一步。这次主要介绍两种保存Model的模块pickle与joblib。

from sklearn.model_selection import validation_curve #学习曲线模块
import sklearn.datasets as datasets
from sklearn.svm import SVC #Support Vector Classifier
import matplotlib.pyplot as plt #可视化模块

clf = SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X,y)

# import pickle #pickle模块

# #保存Model(注:save文件夹要预先建立，否则会报错)
# with open('save/clf.pickle', 'wb') as f:
#     pickle.dump(clf, f)

# #读取Model
# with open('save/clf.pickle', 'rb') as f:
#     clf2 = pickle.load(f)
#     #测试读取后的Model
#     print(clf2.predict(X[0:1]))

# [0]

#jbolib模块
from sklearn.externals import joblib

#save
joblib.dump(clf,'save/clf.joblib')

##读取Model
clf3=joblib.load('save/clf.joblib')

print(clf3.predict(X[0:1]))