from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404
from django.db.models import *
from app.models import *
from app.knn import knnfunc, knn_predict
from app.logistic_regression import logisticfunc
from app.Linear_Discriminant import linearfunc
from app.models import *
from app.models import Parameters
from app.preprocessin import *
from collections import Counter




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
    knnfunc()
    logisticfunc()
    linearfunc()
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    naive = Parameters.objects.filter(algorithm_name = "naive").select_related()[0]    
        
    #knnfunc()
    #preprocess_log()
    

    #get values to display in database
    count_suspicious = len(classified_data.objects.filter(category=1))
    count_total_records = len(classified_data.objects.all())
    count_unsuspicious = len(classified_data.objects.filter(category=0))

    suspicious_records = classified_data.objects.filter(category=1)
    date_list = []
    for suspicious in suspicious_records:
        date_list.append(suspicious.data_set.date)
    count_sus = Counter(date_list)

    date_unique=[]
    count_date=[]
    for count in count_sus:
        date_unique.append(count)
        count_date.append(count_sus[count])


    context = {"svm" : svm,
        "knn" : knn,
        "naive": naive,
        'suspicious':count_suspicious,
        'total':count_total_records,
        'unsuspicious':count_unsuspicious,
        'date_unique':date_unique,
        'count_date':count_date}

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


def preprocess_log():
    latest_id = data_set.objects.all()
    last_id= len(latest_id)
    if latest_id == None:
        last_id = 0

    # Please uncomment these 2 lines while running for the first time
    # change fire3.txt for different firewall log file
    file_add = "C:/Users/Dell/Documents/GitHub/Major-Project/FrontEnd/FrontEnd/app/firewalllog.txt"
    convert_to_csv(file_add, last_id)
    print("converted")

    #predict after preprocessing and store in database
    latest_pred_id = data_set_normalized.objects.all()
    last_pred_id= len(latest_pred_id)
    if latest_pred_id == None:
        last_pred_id = 0
    #get the values from database and use prediction
    cnx = sqlite3.connect("./db.sqlite3")
    df = pd.read_sql("SELECT * FROM app_data_set_normalized WHERE id > (?)",params=(last_pred_id,), con=cnx)
    X = np.array(df.drop(["id","data_set_id"],1))
    y = np.array(len(X))  

    #predict the values
    y_pred = knn_predict(X)    
    #save predicted values into a new database
    print(y_pred)
    df_pred = pd.DataFrame(y_pred)
    df_pred["data_set_id"]=df["data_set_id"]
    df_pred.columns=["category", "data_set_id"]
    #delete the previous database
    #predicted_values = classified_data.objects.all()
    #predicted_values.delete()
    #add new prediction into the database
    df_pred.to_sql(name="app_classified_data",if_exists = "append", con =cnx, index=False)
    print("predicted")


