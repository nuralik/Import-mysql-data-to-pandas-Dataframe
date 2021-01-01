import mysql.connector
import pandas as pd
import numpy as np

class mysql_data:

    def __init__(self, device_id, Start_time, End_time):
        self.device_id = device_id
        self.Start_time = Start_time
        self.End_time = End_time

    def grabData(device_id,Start_time,End_time):
         db_connection=mysql.connector.connect(user='USER_NAME',password='PASS_WORD',host='IP',database='DATA_BASE',use_pure=True)
         db_cursor=db_connection.cursor()
         db_cursor.execute("SELECT * FROM {}  WHERE reg_date BETWEEN '{}' and '{}'".format(device_id,Start_time, End_time))
         df=pd.DataFrame(db_cursor.fetchall())
         return df
    
    
    

     
