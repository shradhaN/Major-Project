from django.conf.urls import url
from app import views
from app.helpers import LogFetcher 

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.homepage, name='homepage'),
    url(r'^svm_knn/$', views.svm_knn, name='svm_knn'),
    url(r'^knn_naive/$', views.knn_naive, name='knn_naive'),
    url(r'^naive_svm/$', views.naive_svm, name='naive_svm'),
    url(r'^three_algo/$', views.three_algo, name='three_algo'),

]
logfetcher = LogFetcher()
logfetcher.start()