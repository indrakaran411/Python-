import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from time import time
from sklearn import tree


def train_svm():

	# Importing the dataset
	dataset = pd.read_csv('Breast Cancer Data.csv')
	X = dataset.iloc[:, 2:32].values
	y = dataset.iloc[:, 1].values

	# Encoding categorical data
	from sklearn.preprocessing import LabelEncoder, OneHotEncoder
	labelencoder_X_1 = LabelEncoder()
	y = labelencoder_X_1.fit_transform(y)

	# Splitting the dataset into the Training set and Test set
	global X_test, y_test
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	global sc
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)

	clf = SVC(probability=True)
	clf.fit(X_train, y_train)
    
	# Train Decision Tree Model
	DTC_Classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=33, random_state=20, max_features=12, splitter='random')
	DTC_Classifier.fit(X_train, y_train)
	print ('DTC Classifier run')
	return clf

def train_DT():

	# Importing the dataset
	dataset = pd.read_csv('Breast Cancer Data.csv')
	X = dataset.iloc[:, 2:32].values
	y = dataset.iloc[:, 1].values

	# Encoding categorical data
	from sklearn.preprocessing import LabelEncoder, OneHotEncoder
	labelencoder_X_1 = LabelEncoder()
	y = labelencoder_X_1.fit_transform(y)

	# Splitting the dataset into the Training set and Test set
	global X_test, y_test
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	global sc
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)

 
    
	# Train Decision Tree Model
	DTC_Classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=33, random_state=20, max_features=12, splitter='random')
	DTC_Classifier.fit(X_train, y_train)
	print ('DTC Classifier run')
	return DTC_Classifier

def test_DT(clf1):
	t = time()
	output = clf1.predict(X_test)
	acc = accuracy_score(y_test, output) 
	print("The accuracy of testing data: ",acc)
	print("The running time: ",time()-t)


def test_svm(clf):
	t = time()
	output = clf.predict(X_test)
	acc = accuracy_score(y_test, output) 
	print("The accuracy of testing data: ",acc)
	print("The running time: ",time()-t)

def predict_DT(clf1, inp):
	t = time()
	inp = sc.transform(inp)
	output = clf1.predict(inp)
	acc = clf1.predict_proba(inp)
	print("The running time: ",time()-t)

	return output, acc, time()-t

def predict_svm(clf, inp):
	t = time()
	inp = sc.transform(inp)
	output = clf.predict(inp)
	acc = clf.predict_proba(inp)
	print("The running time: ",time()-t)

	return output, acc, time()-t