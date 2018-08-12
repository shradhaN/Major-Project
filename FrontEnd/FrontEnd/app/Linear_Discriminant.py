import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from app.models import Parameters
def linearfunc():
	df = pd.read_csv("C:/Users/Dell/Documents/GitHub/Major-Project/ExampleSets/newly_truncated_value.csv")
	df.head()
	X = np.array(df.drop(['5','6','7'],1))
	y = np.array(df['7'])
	y = y.astype("int")
	# Splitting the dataset into the Training set and Test set
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	#Applying Linear Discriminant Analysis
	lda = LinearDiscriminantAnalysis(n_components = 2)
	X_train = lda.fit_transform(X_train, y_train)
	X_test = lda.transform(X_test)
	#Fitting Logistic Regression to the Training set
	classifier =LinearDiscriminantAnalysis()
	classifier.fit(X_train, y_train)
	 # Predicting the Test set results
	y_pred = classifier.predict(X_test)
	a = confusion_matrix(y_test,y_pred)
	tp = a[0][0]
	tn =a[1][1]
	fp = a[0][1]
	fn = a[1][0]
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
	LinearDiscriminantAnalysis(y_test,y_pred)
	pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
	print(classification_report(y_test,y_pred))
	from sklearn.metrics import roc_auc_score
	from sklearn.metrics import roc_curve
	logit_roc_auc = roc_auc_score(y_test, classifier.predict(X_test))
	fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])
	#Area under ROC curve
	roc_auc_score(y_test,y_pred)