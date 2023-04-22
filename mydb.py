import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)

# prepare a cursor object
cur = db.cursor()

# create a database
cur.execute("CREATE DATABASE members")
print("All Done successfully.")
