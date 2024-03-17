from flask import Flask, render_template, request

from svm_func import train_svm, test_svm, predict_svm,train_DT, test_DT, predict_DT

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from time import time


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_method():
	return render_template('home.html')

@app.route('/predict', methods=['POST']) 
def login_user():

	if(request.form['space']=='None'):
		data = []
		string = 'value'
		for i in range(1,31):
			data.append(float(request.form['value'+str(i)]))

		for i in range(30):
			print(data[i])

	else:
		string = request.form['space']
		data = string.split()
		print(data)
		print("Type:", type(data))
		print("Length:", len(data))
		for i in range(30):
			print(data[i])
		data = [float(x.strip()) for x in data]

		for i in range(30):
			print(data[i])

	data_np = np.asarray(data, dtype = float)
	data_np = data_np.reshape(1,-1)
	#out, acc, t = predict_svm(clf, data_np)
	out1, acc1, t1 = predict_DT(clf1, data_np)
	if(out1==1):
		output = 'Malignant'
	else:
		output = 'Benign'

	acc_x = acc1[0][0]
	acc_y = acc1[0][1]
	if(acc_x>acc_y):
		acc1 = acc_x
	else:
		acc1=acc_y
	return render_template('result.html', output=output, accuracy=round(acc1*100,3), time=t1)

@app.route('/profile')
def display():
	return render_template('profile.html')

	
	

if __name__=='__main__':
	global clf 
	clf = train_svm()
	test_svm(clf)
	clf1 = train_DT()
	test_DT(clf1)
	print("Done")
	app.run(port=4995)

