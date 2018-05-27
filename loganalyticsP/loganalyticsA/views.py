from django.shortcuts import render
from django.contrib import auth, messages
from django.conf.urls import url, include
from django.conf import settings

# Create your views here
def homepage(request):
	if request.method == 'POST':
		search_id = request.POST.get('ip_address', None)
		print(search_id)
        
		

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