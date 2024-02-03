import mysql.connector
import json
from flask import make_response


class user_model():
    def __init__(self):
        # try:
            self.con=mysql.connector.connect(host="localhost",password="Akarsh_25",user="root",database="project1")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        # except:
        #     print("some error") 


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM data")
        result=self.cur.fetchall()
        #print(result)
        #query execution code
        if len(result) > 0:
           res = make_response({"payload":result}, 200)
           res.headers['Access-Control-Allow-Origin'] = '*'
           return res
           #return json.dumps(result)
        else:
            return make_response({"message":"No data found"}, 204)
        
        
    def user_addone_model(self, value):
        self.cur.execute(f"INSERT INTO data(s_no,datacol) VALUES('{value['s_no']}','{value['datacol']}')")
        #print(value)
        return {"message":"value added successfully"}
    
    
    def user_delete_model(self,s_no):
        self.cur.execute(f"DELETE FROM data WHERE s_no={s_no}")
        return {"message":"Row deleted successfully"} 
       
    
    # def user_patch_model(self,value,s_no):
    #     # UPDATE user SET col=v
    #     return "this is patch model"
    

    def user_pagination_model(self,limit,page):
        limit = int(limit)
        page = int(page)
        start = (page*limit)-limit
        qry = f"SELECT * FROM data LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        #print(result)
        #query execution code
        
        if len(result) > 0:
           res = make_response({"payload":result, "page_no":page , "limit":limit},200)
           return res   
        else:
            return make_response({"message":"No data found"}, 204)