import sqlite3
def connect_admin1():
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS train80 (trainnumber INTEGER PRIMARY KEY,name text,age integer,gender text,aadharnumber integer,nationality text,source text,destination text,foodservice text,berthpreference text,coach text ,departuretime integer,arrivaltime integer)" )
    conn.commit()
    conn.close()

def insert_admin1(trainnumber,name,age,gender,aadharnumber,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime):
    conn = sqlite3.connect("onlinetrainbooking_2020.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO train80 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(trainnumber,name,age,gender,aadharnumber,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime))
    conn.commit()
    conn.close()

def view_admin1():
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train80")
    rows=cur.fetchall()
    conn.close()
    return rows


def search_admin1(trainnumber="",berthpreference=""):
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train80  WHERE trainnumber=? OR berthpreference=?",(trainnumber,berthpreference))
    rows=cur.fetchall()
    conn.close()
    return rows



def update_admin1(trainnumber,name,age,gender,aadharnumber,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime):
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("UPDATE train80 SET name=?,age=?,gender=?,aadharnumber=?,nationality=?,source=?,destination=?,foodservice=?,berthpreference=?,coach=?,departuretime=?,arrivaltime=? WHERE trainnumber =?",(trainnumber,name,age,gender,aadharnumber,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime))
    conn.commit()
    conn.close()


def delete_admin1(trainnumber):
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM train80 WHERE trainnumber=? ", (trainnumber,))
    conn.commit()
    conn.close()


#connect()

connect_admin1()

#insert_admin1(0987,"bhagya",21,"f",1234,"ind","hindupur","anantapur","yes","lower","s5","9:30","12:00")
#search_admin1(0987)
#print(search_admin1(20,"charan"))

#update_admin1(0987,"bhagya",21,"f",1234,"ind","hindupur","anantapur","yes","lower","s6","9:30","12:00")
#delete_admin1()
print(view_admin1())