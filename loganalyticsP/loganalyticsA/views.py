from django.shortcuts import render
from django.contrib import auth, messages
from django.conf.urls import url, include
from django.conf import settings

from MlModels.knn import predict
from MlModels.svm import Support_Vector_Machine
from sklearn.preprocessing import MinMaxScaler

import socket, struct
from binascii import hexlify
import random
import csv
import pandas as pd
import numpy as np

import pickle
# Create your views here
def homepage(request):
	if request.POST:

		df = pd.read_csv("/home/shradha/virtualenvironment/ML/bin/Major project/loganalyticsP/loganalyticsA/predict-3.csv")
		scaler = MinMaxScaler()
		df[['src-ip']] = scaler.fit_transform(df[['src-ip']])
		for_knn = np.array(df['src-ip']).reshape(-1, 1)

		#print(for_knn)
		category_knn = predict(for_knn)
		print ("for  K mean #################################33##############3")
		print(category_knn)
		print ("for  svm######################################################")
		print(category_knn)


		# predict_us = np.array(df[['src-ip','risk-factor']])

		# csvfile = request.FILES['csv_file']

		# dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
		# csvfile.open()
		# reader = csv.reader(codecs.EncodedFile(csvfile,"utf-8"), delimiter=",", dialect=dialect)
		#search_id = request.POST.get('ip_address', None)
		# ip_integer = ConvertIptoNum(search_id)
		# print(ip_integer)
		# risk_factor_array = [1,5.7,10,4.3,8]
		# input_array_svm = [[ip_integer,random.choice(risk_factor_array)]]
		#print(reader)
		#scaler = MinMaxScaler()
		#input_array_svm = scaler.fit_transform(input_array_svm)
    
		# svm = Support_Vector_Machine()
		# svm = pickle.load(open('/home/shradha/virtualenvironment/ML/bin/Major project/loganalyticsP/MlModels/svm.sav','rb'))
		# for p in predict_us:
		# 	svm.predict(p)

		# svm.visualize()
		

	template_name ='loganalyticsA/homepage.html'
	return render (request, template_name)

def kmean(request):
	template_name ='loganalyticsA/kmean.html'
	return render (request, template_name)

def svm(request):
	template_name ='loganalyticsA/svm.html'
	return render (request, template_name)

def arko(request):
	template_name ='loganalyticsA/arko.html'
	return render (request, template_name)


def ConvertIptoNum(ip):
    try:
        #convert decimal dotted quad string to long integer
        return struct.unpack('>L',socket.inet_aton(ip))[0]
    except Exception:
        return int(hexlify(socket.inet_pton(socket.AF_INET6, ip)), 16)
