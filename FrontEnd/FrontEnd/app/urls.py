from django.conf.urls import url
from app import views
from app.helpers import LogFetcher 

urlpatterns = [

    # The home page
    url(r'^$', views.homepage, name='homepage'),
    url(r'^svm_knn/$', views.svm_knn, name='svm_knn'),
    url(r'^knn_naive/$', views.knn_naive, name='knn_naive'),
    url(r'^naive_svm/$', views.naive_svm, name='naive_svm'),
    url(r'^three_algo/$', views.three_algo, name='three_algo'),

]
# Log fetcher is the  function in helpers.py that pulls the firewall logs 
logfetcher = LogFetcher()
#threading started
logfetcher.start()