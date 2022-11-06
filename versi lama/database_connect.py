from sqlite3 import Cursor
import mysql.connector
    
def database_connect():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty123",
    database = "ontrack",
    auth_plugin = "mysql_native_password"
    )

    return mydb