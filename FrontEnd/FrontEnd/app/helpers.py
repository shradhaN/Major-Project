import threading

from app.models import *
from app.preprocessin import *
from app.knn import knn_predict
import time


class LogFetcher(threading.Thread):
	def run(self):
		while True:
			#users = User.objects.filter(is_superuser = False)
			#print ("running thread",threading.activeCount())
			
			#for user in users:
				
			#   setting = Setting.objects.filter(user_id = user.id )
				
			#   if (setting[0].urls):
			latest_pred_id = data_set_normalized.objects.all()
			last_pred_id= len(latest_pred_id)
			if latest_pred_id == None:
				last_pred_id = 0
			t= threading.Thread(target = self.preprocess_log, args=(last_pred_id,))
			t.start()               
			time.sleep(3600)

	def preprocess_log(self,last_pred_id):
		# threading.Timer(420, preprocess_log).start()
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
