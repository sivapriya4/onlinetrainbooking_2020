import sqlite3
def connect_user1():
     conn=sqlite3.connect("onlinetrainbooking_2020.db")
     cur=conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS train90 (aadharnumber INTEGER PRIMARY KEY ,name text,age integer,gender text,nationality text,source text,destination text,foodservice text,berthpreference text,coach text,departuretime text,arrivaltime text)")
     conn.commit()
     conn.close()


def insert_user1(aadharnumber,name,age,gender,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime):
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO train90 VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(aadharnumber,name,age,gender,nationality,source,destination,foodservice,berthpreference,coach,departuretime,arrivaltime))
    conn.commit()
    conn.close()


def view_user1():
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train90")
    rows=cur.fetchall()
    conn.close()
    return rows




def search_user1(aadharnumber="",name=""):
    conn=sqlite3.connect("onlinetrainbooking_2020.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train90 WHERE aadharnumber=? OR name=?",(aadharnumber,name))
    rows=cur.fetchall()
    conn.close()
    return rows


#connect()
connect_user1()

#insert_user1(7638899,"manisha","20","f","ind","hyd","blr","yes","lower","a","11","6")
#search_user1("manisha")
#update_user1(1234,"bhagya",21,"f","ind","hindupur","anantapur","yes","lower","s5","9:30","12:00")
#print(search_user1(20,"charan"))
#delete()
print(view_user1())
#submit(96317,"momin",30,40,"saudi",)


