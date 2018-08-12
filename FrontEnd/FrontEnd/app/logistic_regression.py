import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from app.models import Parameters


def logisticfunc():
	plt.rc("font", size=14)
	sns.set(style="white")
	sns.set(style="whitegrid", color_codes=True)
	df = pd.read_csv("C:/Users/Dell/Documents/GitHub/Major-Project/ExampleSets/newly_truncated_value.csv")
	df.head()
	X = np.array(df.drop(['5','6','7'],1))
	y = np.array(df['7'])
	y = y.astype("int")
	#Logistic Regression Model Fitting
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
	#Cross Validation

	kfold = model_selection.KFold(n_splits=10, random_state=7)
	modelCV = LogisticRegression()
	scoring = 'accuracy'
	results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
	print("10-fold cross validation average accuracy: %.3f" % (results.mean()))
	#Confusion Matrix
	a = confusion_matrix(y_test,y_pred)
	tp = a[0][0]
	tn =a[1][1]
	fp = a[0][1]
	fn = a[1][0]
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
	z = Parameters(tp = tp, tn = tn, fp = fp, fn = fn, algorithm_name = name, precision = precision, accuracy = accuracy, hit = hit, tnr = tnr, miss = miss, fallout = fallout, f1score= f1score)
	z.save()
	pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
	#Compute precision, recall, F-measure and support
	print(classification_report(y_test, y_pred))
	logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
	fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])

	#Area under ROC curve
	roc_auc_score(y_test,y_pred)