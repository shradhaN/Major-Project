from django.conf.urls import url, include
from django.contrib import admin
from loganalyticsA import views
from django.conf import settings

urlpatterns =[
url(r'^homepage/$',views.homepage, name = 'homepage'),
url(r'^kmean/$',views.kmean, name = 'kmean'),
url(r'^svm/$',views.svm, name = 'svm'),
url(r'^arko/$',views.arko, name = 'arko'),

]


