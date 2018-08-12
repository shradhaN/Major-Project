import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
#import classification_report
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
#Area under ROC curve
from sklearn.metrics import roc_auc_score
#import GridSearchCV
from sklearn.model_selection import GridSearchCV
from app.models import *



#svmknn
def knnnewfunc():

	plt.style.use('ggplot')
	df = pd.read_csv("C:/Users/Dell/Documents/GitHub/Major-Project/ExampleSets/Firewall_final_normalized.csv")

	df.head()
	df.shape
	X = np.array(df.drop(['5','6','7'],1))
	y = np.array(df['7'])
	y = y.astype("int")
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=42, stratify=y)
	neighbors = np.arange(1,7)
	train_accuracy =np.empty(len(neighbors))
	test_accuracy = np.empty(len(neighbors))

	for i,k in enumerate(neighbors):
	     #Setup a knn classifier with k neighbors
	    knn = KNeighborsClassifier(n_neighbors=k)
	    
	    #Fit the model
	    knn.fit(X_train, y_train)
	    
	    #Compute accuracy on the training set
	    train_accuracy[i] = knn.score(X_train, y_train)
	    
	    #Compute accuracy on the test set
	    test_accuracy[i] = knn.score(X_test, y_test) 
	#Setup a knn classifier with k neighbors
	knn = KNeighborsClassifier(n_neighbors=2)
	#Fit the model
	knn.fit(X_train,y_train)
	filename = "knn-suravi.sav"
	pickle.dump(knn, open(filename,'wb'))
	loaded_model = pickle.load(open(filename,'rb'))
	accuracy = loaded_model.score(X_test, y_test)


	#Get accuracy. Note: In case of classification algorithms score method represents accuracy.
	knn.score(X_test,y_test)
	#let us get the predictions using the classifier we had fit above
	y_pred = knn.predict(X_test)
	a = confusion_matrix(y_test,y_pred)
	tp = a[0][0]
	tn =a[1][1]
	fp = a[0][1]
	fn = a[1][0]
	name = "knn_train"

	lengthofy = list(y_test)
	positive = lengthofy.count(0)
	negative = lengthofy.count(1)

	q = actual_value(positive = positive, negative = negative)
	q.save()

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
	z = Parameters(tp = tp, tn = tn, fp = fp, fn = fn, algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
	z.save()
	pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
	print(classification_report(y_test,y_pred))
	y_pred_proba = knn.predict_proba(X_test)[:,1]
	fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

	roc_auc_score(y_test,y_pred_proba)


def knn_predict(x):
	loaded_model = pickle.load(open("knn-suravi.sav",'rb'))
	return loaded_model.predict(x)
