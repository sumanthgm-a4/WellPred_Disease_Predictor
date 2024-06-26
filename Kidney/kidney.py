# -*- coding: utf-8 -*-
"""Kidney.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WjmYKrPXmW5_O_VTFYHlLcBylb4v29Nl
"""

import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("kidney.csv")
data.head()

data.isnull().sum()

data['classification'].value_counts()

data['classification']=data['classification'].replace('ckd\t','ckd')
data['classification'].value_counts()

data = data.drop("id", axis = 1)

data.info()

data=data.drop_duplicates()

from sklearn.preprocessing import LabelEncoder

for i in data.columns:
    if data[i].dtype=='object':
        data[i]=LabelEncoder().fit_transform(data[i])
data.info()

from sklearn.impute import KNNImputer

imp = KNNImputer(n_neighbors = 5)
data_p = imp.fit_transform(data)
data_p = pd.DataFrame(data_p, columns = data.columns)
data_p.isnull().sum()

mnop = data.to_csv("Preprocessed_dataset.csv")

y = np.array(data_p['classification'])
y = y.reshape(-1, 1)
X = np.array(data_p.drop(['classification'], axis = 1))

print(X)
print(y)

print("Before oversampling, counts of label '0': {}".format(sum(y == 0)))
print("Before oversampling, counts of label '1': {}".format(sum(y == 1)))

# SPLITTING DATA INTO TRAIN AND TEST DATASETS
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

!pip install lazypredict

from lazypredict.Supervised import LazyClassifier

clf = LazyClassifier(verbose = 0, ignore_warnings = True, custom_metric = None)

models, predictions = clf.fit(X_train, X_test, y_train, y_test)
models

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print(accuracy_score(y_test, y_pred))
print()
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred))

y_pred = log_reg.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

import joblib

joblib.dump(value = [data_p, scaler, log_reg], filename = "/content/kidney_models.pkl")

abc = data_p.to_csv("Preprocessed_dataset.csv")

