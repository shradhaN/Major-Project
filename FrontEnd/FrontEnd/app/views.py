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
    precision = round(precision*100,2)
    accuracy = (tp+ tn)/(tp+tn+fp+fn)
    accuracy = round(accuracy *100,2)
    hit = (tp)/(tp+fn)# recall, hit rate, true postive rate
    hit = round(hit*100,2)
    tnr = (tn)/(tn+fp)
    tnr = round(tnr*100,2)
    miss = fn/(fn+tn)# miss rate, false negativve rate
    miss =  round(miss*100,2)
    fallout = fp/(fn+tp)#false positive rate
    fallout = round(fallout *100,2)
    f1score = round(2*(hit*precision)/(hit+precision),2)#if you have an uneven class distribution. 
    p = Parameters(algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
    p.save()

    tp = 789
    tn =469
    fp = 20
    fn = 56
    name = "knn"
    precision =  (tp)/(tp+fp)#positive prediction value
    precision = round(precision*100,2)
    accuracy = (tp+ tn)/(tp+tn+fp+fn)
    accuracy = round(accuracy *100,2)
    hit = (tp)/(tp+fn)# recall, hit rate, true postive rate
    hit = round(hit*100,2)
    tnr = (tn)/(tn+fp)
    tnr = round(tnr*100,2)
    miss = fn/(fn+tn)# miss rate, false negativve rate
    miss =  round(miss*100,2)
    fallout = fp/(fn+tp)#false positive rate
    fallout = round(fallout *100,2)
    f1score = round(2*(hit*precision)/(hit+precision),2)#if you have an uneven class distribution. 
    q = Parameters(algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
    q.save()

    tp = 539
    tn =129
    fp = 90
    fn = 20
    name = "naive"
    precision =  (tp)/(tp+fp)#positive prediction value
    precision = round(precision*100,2)
    accuracy = (tp+ tn)/(tp+tn+fp+fn)
    accuracy = round(accuracy *100,2)
    hit = (tp)/(tp+fn)# recall, hit rate, true postive rate
    hit = round(hit*100,2)
    tnr = (tn)/(tn+fp)
    tnr = round(tnr*100,2)
    miss = fn/(fn+tn)# miss rate, false negativve rate
    miss =  round(miss*100,2)
    fallout = fp/(fn+tp)#false positive rate
    fallout = round(fallout *100,2)
    f1score = round(2*(hit*precision)/(hit+precision),2)#if you have an uneven class distribution. 
    z = Parameters(algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
    z.save()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    naive = Parameters.objects.filter(algorithm_name = "naive").select_related()[0]
    # svm =0
    # knn = 0

    context = {"a":a, "svm" : svm,
        "knn" : knn,
        "naive": naive}
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
    naive = Parameters.objects.filter(algorithm_name = "naive").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    context = {'naive': naive,
        'knn':knn
        }
    template = loader.get_template('app/major/knn_naive.html')
    return HttpResponse(template.render(context, request))

def naive_svm(request):
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    naive = Parameters.objects.filter(algorithm_name = "naive").select_related()[0]
    context = {'svm': svm,
        'naive':naive
        }
    template = loader.get_template('app/major/naive_svm.html')
    return HttpResponse(template.render(context, request))

def three_algo(request):
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    naive = Parameters.objects.filter(algorithm_name = "naive").select_related()[0]
    
    context = {'svm': svm,
        'knn':knn,
        'naive':naive
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

