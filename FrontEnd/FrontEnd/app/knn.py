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

def knnfunc():

	plt.style.use('ggplot')
	df = pd.read_csv("/home/suravi/Major-Project/FrontEnd/FrontEnd/app/static/dataset/Firewall_final_normalized.csv")

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
	#Generate plot
	plt.title('k-NN Varying number of neighbors')
	plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
	plt.plot(neighbors, train_accuracy, label='Training accuracy')
	plt.legend()
	plt.xlabel('Number of neighbors')
	plt.ylabel('Accuracy')
	plt.savefig("knn.png")#save inside static/images
	#plt.show()
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
	confusion_matrix(y_test,y_pred)
	pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
	print(classification_report(y_test,y_pred))
	y_pred_proba = knn.predict_proba(X_test)[:,1]
	fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

	plt.plot([0,1],[0,1],'k--')
	plt.plot(fpr,tpr, label='Knn')
	plt.xlabel('fpr')
	plt.ylabel('tpr')
	plt.title('Knn(n_neighbors=7) ROC curve')
	plt.savefig("knnroc.png")
	#plt.show()


	roc_auc_score(y_test,y_pred_proba)


def predict(x):
	loaded_model = pickle.load(open("knn-suravi.sav",'rb'))
	return loaded_model.predict(x)
