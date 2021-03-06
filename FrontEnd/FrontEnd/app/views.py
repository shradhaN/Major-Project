from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse,render_to_response,get_object_or_404
from django.db.models import *
from app.models import *
from app.knn import knnfunc, predict
from app.knn_new import knnnewfunc, knn_predict
from app.logistic_regression import logisticfunc

from app.models import *
from app.models import Parameters
from app.preprocessin import *
from collections import Counter
import threading




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
    Parameters.objects.all().delete()   
    knnfunc()
    logisticfunc()
    
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    #knnfunc()
    #predict after preprocessing and store in database
    latest_pred_id = data_set_normalized.objects.all()
    last_pred_id= len(latest_pred_id)
    if latest_pred_id == None:
        last_pred_id = 0
    #preprocess_log(last_pred_id)   

    #get values to display in database
    count_suspicious = classified_data.objects.filter(category=1).count()
    count_total_records = classified_data.objects.all().count()
    count_unsuspicious = classified_data.objects.filter(category=0).count()
    if count_total_records ==0:
        suspicious_percentage = 0
        unsuspicious_percentage = 0
    else:
        suspicious_percentage = (count_suspicious/count_total_records)*100
        unsuspicious_percentage = (count_unsuspicious/count_total_records)*100

    #for suspiciious
    suspicious_records = classified_data.objects.filter(category=1)
    date_list = []
    stcp=0
    sudp=0
    sicmp=0
    ssend=0
    sreceive=0
    saction=0
    sallow=0
    sdeny=0
    spath=0
    for suspicious in suspicious_records:
        #protocol
        if suspicious.data_set.protocol == "0":
            sudp=sudp+1
        if suspicious.data_set.protocol == "1":
            stcp=stcp+1
        if suspicious.data_set.protocol == "2":
            sicmp=sicmp+1

        #action
        if suspicious.data_set.action == "0":
            sallow=sallow+1
        if suspicious.data_set.action == "1":
            sdeny=sdeny+1
        if suspicious.data_set.action == "-9999":
            saction=saction+1

        #path
        if suspicious.data_set.path == 0:
            sreceive=sreceive+1
        if suspicious.data_set.path == 1:
            ssend=ssend+1
        if suspicious.data_set.path == -9999:
            spath=spath+1
        date_list.append(suspicious.data_set.date)
    count_sus = Counter(date_list)

    date_unique=[]
    count_date=[]
    for count in count_sus:
        date_unique.append(count)
        count_date.append(count_sus[count])

    #for unsuspicious
    unsuspicious_records = classified_data.objects.filter(category=0)
    unsuspicious_date_list=[]
    for unsuspicious in unsuspicious_records:
        unsuspicious_date_list.append(unsuspicious.data_set.date)
    count_unsus = Counter(unsuspicious_date_list)
    date_unique_un=[]
    count_unique_un=[]
    for count in count_unsus:
        date_unique_un.append(count)
        count_unique_un.append(count_unsus[count])


    #action and protocols
    udp_count = data_set.objects.filter(protocol=0).count()
    tcp_count = data_set.objects.filter(protocol=1).count()
    icmp_count=data_set.objects.filter(protocol=2).count()
    unknown_count = data_set.objects.filter(protocol=-99999).count()
    total_protocol = udp_count+tcp_count+icmp_count+unknown_count

    if total_protocol == 0:
        udp_percent=0
        tcp_percent=0
        unknown_percent=0
        icmp_percent=0
    else:
        udp_percent=(udp_count/total_protocol)*100
        tcp_percent=(tcp_count/total_protocol)*100
        icmp_percent=(icmp_count/total_protocol)*100
        unknown_percent=(unknown_count/total_protocol)*100




    context = {"svm" : svm,
        "knn" : knn,
      
        'suspicious':count_suspicious,
        'total':count_total_records,
        'unsuspicious':count_unsuspicious,
        'date_unique':date_unique,
        'count_date':count_date,
        "date_unique_unsus":date_unique_un,
        "count_unique_un":count_unique_un,
        'sus_percent':suspicious_percentage,
        "unsus_percent":unsuspicious_percentage,
        'udp_percent':udp_percent,
        "tcp_percent":tcp_percent,
        "icmp_percent":icmp_percent,
        "unknown_percent":unknown_percent,
        "stcp" : stcp,
        "sudp" : sudp,
        "sicmp" : sicmp,
        "ssend" : ssend,
        "sreceive" :sreceive, 
        "saction" : saction,
        "sallow" : sallow,
        "sdeny" : sdeny,
        "spath" : spath
        }

    template = loader.get_template('app/major/homepage.html')
    return HttpResponse(template.render(context, request))



def svm_knn(request):
   
    svm = Parameters.objects.filter(algorithm_name = "svm").select_related()[0]
    knn = Parameters.objects.filter(algorithm_name = "knn").select_related()[0]
    actual = actual_value.objects.all()[0]
    context = {'svm': svm,
        'knn':knn,
        'actual':actual
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


def preprocess_log(last_pred_id):
    #threading.Timer(420, preprocess_log).start()
    latest_id = data_set.objects.all()
    last_id= len(latest_id)
    if latest_id == None:
        last_id = 0

    # Please uncomment these 2 lines while running for the first time
    # change fire3.txt for different firewall log file
    file_add = "C:/Users/Dell/Documents/GitHub/Major-Project/FrontEnd/FrontEnd/app/firewalllog.txt"
    convert_to_csv(file_add, last_id)
    print("converted")

    #get the values from database and use prediction
    cnx = sqlite3.connect("./db.sqlite3")
    df = pd.read_sql("SELECT * FROM app_data_set_normalized WHERE id > (?)",params=(last_pred_id,), con=cnx)
    #df = pd.read_sql("SELECT * FROM app_data_set_normalized", con=cnx)
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





