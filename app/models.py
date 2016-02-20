import sqlite3 as sql
def insert_article(title,descrip,timestamp):
    con = sql.connect("database")  
    cur = con.cursor()
    id=1
    cur.execute("INSERT INTO account_holder (title,descrip,timestamp) VALUES (?,?,?) ,(title,descrip,timestamp)")
    con.commit()
    con.close()
    return true



def select_account_holder(params=()):
    con = sql.connect("database")
    cur = con.cursor()
    if params==():
       cur.execute("select * from account_holder")
    else:
       string = "select"
       for i in xrange(len(params)-1):
           string += "%s,"
           string += "%s"
           string += " from account_holder"

       result = cur.execute(string)
       con.close()
       return result.fetchall()
def select_all():
    con = sql.connect("database")
    cur = con.cursor()
    s="SELECT * FROM account_holder"
    result=cur.execute(string)
    con.close()
    return result.fetchall()
