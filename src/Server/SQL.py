import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'user',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'vechicleTrack',
  'raise_on_warnings': True,
  'use_pure': False,
}

def getDB():
    # Get a connection to the database.
    try:
        con =  mysql.connector.connect(**config)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Login failed, user or password incorrect.\n")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database Does not exist\n")
        else: print(error)
    else: con.close()
    return con


def runSQL(sql):
    db = getDB()
    cur = db.cursor()
    cur.execute_query(sql)

