import psycoph2
from psycoph2 import errorcode
import json
# TODO: Convert this to use postgresql.
# TODO: Convert this to use named paramiters within SQL
# http://initd.org/psycopg/docs/usage.html


with open('conf.json') as dataFile:
    config = json.load(dataFile)


def getdb(database):
    # Get a connection to the database.
    config["Database"] = database
    try:
        con = psycoph2.connect(**config)

    except psycoph2.connector.Error as error:
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


def query(database, data):
    db = getdb(database)
    cur = db.cursor()
    content = json.loads(data)
    sql = "SELECT " + "%s, "*(len(content["Fields"]))
    sql += " FROM " + "%s, "*(len(content["Tables"]))
    if content["Keys"]:
        sql += "WHERE " + "%s = %s AND "*(len(content["Keys"])-1)
        sql += "%s = %s"

    cur.execute_query(sql, content["Fields"], content["Tables"],
                      content["Keys"])
    rows = cur.fetchall()
    return rows  # This will not do what I want.


def enter(database, data):
    db = getdb(database)
    cur = db.cursor()
    content = json.loads(data)
    sql = "INSERT INTO " + content["Tables"][0]
    sql += " (" + content["Keys"]["Key"].split(',') + ") "
    sql += "VALUES (" + content["Keys"]["Value"]
    if not content["Test"]:
        sql += " WHERE " + content["Tests"]["Key"] + "=" + content["Tests"]["Value"]

    for key in content["Keys"]:
        sql += key["Key"] + " = " + key["Value"]

    cur.execute(sql)
