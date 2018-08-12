import threading
from app.models import *
from app.preprocessin import *
from app.knn import knn_predict
import time


class LogFetcher(threading.Thread):

	def run(self):
		while True:
			latest_pred_id = data_set_normalized.objects.all()
			last_pred_id= len(latest_pred_id)
			if latest_pred_id == None:
				last_pred_id = 0
			t= threading.Thread(target = self.preprocess_log, args=(last_pred_id,))
			# target function is preporcess_log
			t.start()               
			time.sleep(3600)
			#sleep for 1 hour

	def preprocess_log(self,last_pred_id):
		latest_id = data_set.objects.all()
		last_id= len(latest_id)
		if latest_id == None:
			last_id = 0

		#address where powershell script copies the logs in txt file
		file_add = "C:/Users/Dell/Documents/GitHub/Major-Project/FrontEnd/FrontEnd/app/firewalllog.txt"

		#preprocess txt file and save normailzed data in data_set_normalized model
		convert_to_csv(file_add, last_id)

		#get the values from database and use prediction
		cnx = sqlite3.connect("./db.sqlite3")
		df = pd.read_sql("SELECT * FROM app_data_set_normalized WHERE id > (?)",params=(last_pred_id,), con=cnx)

		if len(df)==0:
			print("no new entries")
		else:	
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
			#add new prediction into the database
			df_pred.to_sql(name="app_classified_data",if_exists = "append", con =cnx, index=False)
			print("predicted")
