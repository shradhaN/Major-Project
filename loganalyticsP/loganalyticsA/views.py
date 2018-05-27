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

import pickle
# Create your views here
def homepage(request):
	if request.method == 'POST':
		search_id = request.POST.get('ip_address', None)
		ip_integer = ConvertIptoNum(search_id)
		print(ip_integer)
		risk_factor_array = [1,5.7,10,4.3,8]
		input_array_svm = [[ip_integer,random.choice(risk_factor_array)]]
		
		scaler = MinMaxScaler()
		input_array_svm = scaler.fit_transform(input_array_svm)
    
		#svm = Support_Vector_Machine()
		#svm = pickle.load(open('/home/shradha/virtualenvironment/ML/bin/Major project/loganalyticsP/MlModels/svm.sav','rb'))
		predict(input_array_svm)
		visualize()
		

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
