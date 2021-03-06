# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F42jRtDF7leex2NflRiP5iMi3oB8Z6Ul
"""

#you start by adding the libraries that you are going to use in the program
import matplotlib.pyplot as plt
import numpy as np
import pandas
 
#we use the iris_dataset and the "load_iris" to stablish some form of dictionary
from sklearn.datasets import load_iris
iris_dataset = load_iris()
 
#we use this keys to order the species of flowers we want to predict based on factors like their features, names, colors, etc
print("keys if iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193]+"\n...")
print("target names: \n{}".format(iris_dataset['target_names']))
print("Feature names: \n{}".format(iris_dataset['feature_names']))
print("type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))
print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))
print("Type of target: {}".format(type(iris_dataset['target'])))
print("Shape of target: {}".format(iris_dataset['target'].shape))
print("Target:\n{}".format(iris_dataset['target']))
 
#this code is used to shuffle the data in a pseudo random state to get a better result from the artificial inteligence
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
 
#the code is then separated and printed using x and y coordinates
print("x_train shape: {}".format(x_train.shape))
print("y_train sahpe: {}".format(y_train.shape))
print("x_test shape: {}".format(x_test.shape))
print("y_test sahpe: {}".format(y_test.shape))
 
#now the columns are labeled using this string of code
iris_dataframe = pd.dataframe(x_train, columns=iris_dataset.feature_names)
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
 
#this encapsulates the data that will be used for the training algorithm in order to predict the new data points
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
#it takes the data into the corresponding training labels
knn.fit(x_train, y_train)
 
#this is used to predict the information and organize it
x_new = np.array([[2, 2.9, 1, 0.2]])
print("X_new.shape: {}".format(x_new.shape))
prediction = knn.predict(x_new)
print("Prediction: {}".format(prediction))
print("Prediction target name: {}".format(iris_dataset['target_names'][prediction]))
y_pred = knn.predict(x_test)
print("Test set predictions:\n {}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(x_test, y_test)))
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
 
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
 
#its used to reveal the precition of the model
print("Test set score: {:.2f}".format(knn.score(x_test, y_test)))