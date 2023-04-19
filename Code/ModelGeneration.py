import numpy as np
import sklearn as sk
from sklearn import tree, gaussian_process, ensemble, feature_selection, pipeline, model_selection
from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd

data = pd.read_csv('Data/train.csv')
#trainTarget = train.pop('prognosis')
#print(train.head())
#print(trainTarget.head())
#print(trainTarget.shape)

trainX, testX = model_selection.train_test_split(data,random_state=1,train_size=0.7,shuffle=True)

trainY = trainX.pop('prognosis')
testY = testX.pop('prognosis')

print(trainX.head())
print(trainY.head())

model = sk.linear_model.LogisticRegression()
model.fit(trainX[['sudden_fever','headache']],trainY)
print(model.classes_)
trainPredictions = model.predict_proba(trainX[['sudden_fever','headache']])
testPredictions = model.predict_proba(testX[['sudden_fever','headache']])

print(trainPredictions)
print(testPredictions)