import pickle
import imp
import sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn import linear_model


data = pd.read_csv('student-mat.csv', sep=';')
print(data.head)

# data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]
# print(data.head)

# X = np.array(data.drop(["G3"], 1))
# y = np.array(data['G3'])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model = linear_model.LinearRegression()

# model.fit(X_train, y_train)
# acc = model.score(X_test, y_test)
# print(acc)

# res = model.predict([ [5, 6, 2, 0, 6] ])
# print(res)

# with open('model.pickle', 'wb') as f:
#     pickle.dump(model, f)

pickle_in = open('model.pickle', 'rb')
linear = pickle.load(pickle_in)
pred = linear.predict([ [3, 9, 2, 0, 6] ])
print(pred)