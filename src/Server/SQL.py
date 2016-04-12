import mysql.connector
from mysql.connector import errorcode
import json

config = {
  'user': 'user',
  'password': 'password',
  'host': '127.0.0.1',
  'database': '',
  'raise_on_warnings': True,
  'use_pure': False,
}


def getDB(database):
    # Get a connection to the database.
    config["Database"] = database
    try:
        con = mysql.connector.connect(**config)

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Login failed, user or password incorrect.\n")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database Does not exist\n")
        else: print(error)
        if con is not None:
            con.close()

    else:
        con.close()
    finally:
        config["Database"] = ""
        return con


def query(data):
    db = getDB(json.loads(data)["Database"])
    cur = db.cursor()
    content = json.loads(data)
    sql = "SELECT " + content["Fields"].split(',')
    sql += " FROM " + content["Tables"][0]
    sql += " Where "
    for key in content["Keys"]:
        sql += key["Key"] + " = " + key["Value"]

    cur.execute_query(sql)
    rows = cur.fetchall()
    return rows  # This will not do what I want.


def enter(data):
    db = getDB(json.loads(data)["Database"])
    cur = db.cursor()
    content = json.loads(data)
    sql = "INSERT INTO  " + content["Fields"].split(',')
    sql += " FROM " + content["Tables"][0]
    sql += " Where "
    for key in content["Keys"]:
        sql += key["Key"] + " = " + key["Value"]

    cur.execute(sql)
