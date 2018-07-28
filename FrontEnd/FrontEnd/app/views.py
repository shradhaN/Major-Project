from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404
from django.db.models import *
from app.models import *

def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


# def gentella_html(request):
#     context = {}
#     # The template to be loaded as per gentelella.
#     # All resource paths for gentelella end in .html.

#     # Pick out the html file name from the url. And load that template.
#     # load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/major/' + load_template)
#     return HttpResponse(template.render(context, request))


def homepage(request):

    context = {}
    template = loader.get_template('app/major/homepage.html')
    return HttpResponse(template.render(context, request))

def svm_knn(request):
    ref_m_count = 20
    ref_f_count = 10
    a =8
    b = 70
    context = {'ref_m_count': ref_m_count,
        'ref_f_count':ref_f_count,
        'a':a,
        'b':b,
        }
    template = loader.get_template('app/major/svm_knn.html')
    return HttpResponse(template.render(context, request))

def knn_naive(request):
    ref_m_count = 20
    ref_f_count = 10
    a =8
    b = 70
    context = {'ref_m_count': ref_m_count,
        'ref_f_count':ref_f_count,
        'a':a,
        'b':b,
        }
    template = loader.get_template('app/major/knn_naive.html')
    return HttpResponse(template.render(context, request))

def naive_svm(request):
    ref_m_count = 20
    ref_f_count = 10
    a =8
    b = 70
    context = {'ref_m_count': ref_m_count,
        'ref_f_count':ref_f_count,
        'a':a,
        'b':b,
        }
    template = loader.get_template('app/major/naive_svm.html')
    return HttpResponse(template.render(context, request))

def three_algo(request):
    ref_m_count = 20
    ref_f_count = 10
    a =8
    b = 70
    context = {'ref_m_count': ref_m_count,
        'ref_f_count':ref_f_count,
        'a':a,
        'b':b,
        }
    template = loader.get_template('app/major/three_algo.html')
    return HttpResponse(template.render(context, request))

