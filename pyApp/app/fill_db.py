import mysql.connector as mysql
import pandas as pd 
import os, sys, traceback

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.csv" ))
df.fillna("NULL")
def create_table():
    command  = """CREATE TABLE chockolate (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        Image VARCHAR(40),
        Chockolate_type VARCHAR(20),
        Name VARCHAR(40),
        Date DATE,
        Weight VARCHAR(20),
        Pack_type VARCHAR(30)
        )"""
    try:
        cur.execute(command)
        db_conn.commit()
   
    except Exception as err:
        e = sys.exc_info()[2]
        tbinfo = traceback.format_tb(e)[0]
        print(err,"\n",tbinfo,)

# print(df.head(5))
host = "localhost"
database = "main_db"
user="root"
passwd = "P@ssw0rd"

db_conn = mysql.connect(host=host,database=database,user=user, password=passwd)
print(db_conn.get_server_info())
cur = db_conn.cursor()
# create_table()
for row in df.iterrows():
    command = "INSERT INTO chockolate (Image,Chockolate_type,Name, Date, Weight, Pack_type) VALUES (%s,%s,%s,%s,%s,%s)"
    row = row[1]
    
    
    Image = row["Image"]
    Chockolate_type = row["Chockolate_type"]
    Name = row["Name"]
    Date = row["Date"]
    if type(Date)==float:
        Date = "NULL"
    Weight = row["Weight"]
    Pack_type = row["Pack_type"]
    data = [Image,Chockolate_type,Name, Date, Weight, Pack_type]
    # for field in data:
    #     print(type(field),field)
    # print(data)

    
    
    try:
        cur.execute(command, data)
        db_conn.commit()

    except Exception as err:
        e = sys.exc_info()[2]
        tbinfo = traceback.format_tb(e)[0]
        print(err,"\n",tbinfo,)
    




