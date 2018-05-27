
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.metrics import confusion_matrix

df = pd.read_csv("/home/shradha/virtualenvironment/ML/bin/Major project/loganalyticsP/MlModels/Final-Normalized-Neumeric-Train(1500).csv")
#df.replace('?',-99999, inplace = True)
#df.drop(['id'],1,inplace = True)
#df.dropna(inplace = True)
#scaler = MinMaxScaler()
#df[['src-ip']] = scaler.fit_transform(df[['src-ip']])
X = np.array(df['src-ip']).reshape(-1, 1)
y = np.array(df['Categories'])
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train,y_train)
filename = "knn-scikit.sav"
pickle.dump(clf, open(filename,'a'))
loaded_model = pickle.load(open(filename,'rb'))
accuracy = loaded_model.score(X_test, y_test)
print(accuracy)

#prediction = loaded_model.predict()
#print(prediction)

#confusion_matrix(y_true, y_test)
#example_measures = np.array([01879435980.0,5.7])
#example_measures = example_measures.reshape(1, -1)
#prediction = clf.predict(example_measures)
#print(prediction)


def predict(x):
	return loaded_model.predict(x)