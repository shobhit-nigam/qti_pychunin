import time
import os
import sqlite3

class DataBaseManager():
    def __init__(self, dbName, hostname=None, port=None, path=os.getcwd()):
        self.dbName = dbName
        self.path = path

    def __enter__(self):
        if self.dbName in os.listdir(self.path):
            print("db is present")
            self.flag = 1
        else:
            self.flag = 0
            print("database not available")
            # raise an exception
        return self

    def connect(self):
        self.con = sqlite3.connect(self.dbName)
        cur = dbObject.con.cursor()
        return cur

    def __exit__(self, x, y, z):
        if self.flag == 1:
            self.con.close()
        print("exiting now")

with DataBaseManager("movies.db") as dbObject:
    # code to work with DB
    print("working with database")
    cur = dbObject.connect()
    query = "SELECT * FROM actors"
    cur.execute(query)
    for x in cur.fetchall():
        print(x)

    time.sleep(5)

print("outside the 'with' block")
