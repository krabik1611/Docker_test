from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import os,sys,traceback
import mysql.connector as mysql

class Database:
    def __init__(self):
        try:
            self.host = os.environ["DB_IP"]
            self.database = os.environ["MYSQL_DATABASE"]
            self.user = os.environ["MYSQL_USER"]
            self.passwd = os.environ["MYSQL_PASSWORD"]
            self.db_conn = mysql.connect(host=self.host,database=self.database,user=self.user, password=self.passwd)
            self.cur = self.db_conn.cursor()
        except Exception as err:
            e = sys.exc_info()[2]
            tbinfo = traceback.format_tb(e)[0]
            print(err,"\n",tbinfo,)
            sys.exit(-1)

    def fetchData(self,how:str=id, where:str="chockolate",pred:str=""):
        try:
            command = f"""SELECT {how} FROM {where} {pred}"""
            self.cur.execute(command)
            answer = self.cur.fetchall()
            print(answer)
        except Exception as err:
            e = sys.exc_info()[2]
            tbinfo = traceback.format_tb(e)[0]
            print(err,"\n",tbinfo,)
        else:
            if how=="*":
                fields = ["id","Image","Chockolate_type","Name","Date","Weight","Pack_type"]
            else:
                fields = how.split(",")
            data = []
            for n in answer:
                temp = {fields[i].encode("utf-8"):n[i].encode("utf-8") for i in range(len(n))}
                data.append(temp)
            return data




app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def home():
    return "Homepage! Welcome!!!"

@app.get("/api/data/getList")
async def getAllList(start:Optional[int]=0,end:Optional[int]=20):
    database = Database()
    answer = database.fetchData(how="*", pred="WHERE id>={} AND id<={}".format(start,end))
    return answer