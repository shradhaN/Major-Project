from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404
from django.db.models import *
from app.models import *
from app.knn import knnfunc, predict
from app.models import *
from app.models import Parameters




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

    
   # knnfunc()
    x = [[1.0,0.0,6.0744851518415993e-30,8.554671662880071e-30,5.0]]
    a = predict(x)
    print(a)
    tp = 565
    tn =469
    fp = 35
    fn = 90
    name = "svm"
    precision =  (tp)/(tp+fp)#positive prediction value
    precision =int( precision *1000 )
    accuracy = (tp+ tn)/(tp+tn+fp+fn)
    accuracy =int( accuracy *1000 )
    hit = (tp)/(tp+fn)# recall, hit rate, true postive rate
    hit =int( hit *1000 )
    tnr = (tn)/(tn+fp)
    tnr =int( tnr *1000 )
    miss = fn/(fn+tn)# miss rate, false negativve rate
    miss =int( miss *1000 )
    fallout = fp/(fn+tp)#false positive rate
    fallout =int( fallout *1000 )
    f1score = 2*(hit*precision)/(hit+precision)#if you have an uneven class distribution. 
    f1score =int( f1score )
    p = Parameters(algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
    p.save()

    tp = 789
    tn =469
    fp = 20
    fn = 56
    name = "knn"
    precision =  (tp)/(tp+fp)#positive prediction value
    precision =int( precision *1000 )
    accuracy = (tp+ tn)/(tp+tn+fp+fn)
    accuracy =int( accuracy *1000 )
    hit = (tp)/(tp+fn)# recall, hit rate, true postive rate
    hit =int( hit *1000 )
    tnr = (tn)/(tn+fp)
    tnr =int( tnr *1000 )
    miss = fn/(fn+tn)# miss rate, false negativve rate
    miss =int( miss *1000 )
    fallout = fp/(fn+tp)#false positive rate
    fallout =int( fallout *1000 )
    f1score = 2*(hit*precision)/(hit+precision)#if you have an uneven class distribution. 
    f1score =int( f1score  )
    q = Parameters(algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
    q.save()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    # svm =0
    # knn = 0

    context = {"a":a, "svm" : svm,
        "knn" : knn}
    template = loader.get_template('app/major/homepage.html')
    return HttpResponse(template.render(context, request))


























def svm_knn(request):
   
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    context = {'svm': svm,
        'knn':knn
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

def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)
 
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
 
    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
 
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")

