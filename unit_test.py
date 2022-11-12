import pytest
import mysql.connector

from manageActivity import manageActivity

def conn():
    try:
        conn = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "qwerty123", 
            database = "ontrack", 
            auth_plugin = "mysql_native_password"
        )
        return conn
    except Exception as e:
        print(e)

def test_addActivity():
    mydb = conn()
    cursor = mydb.cursor()
    sql = "INSERT INTO List_of_Activities (ActivityName, CategoryName, Deadline, isDone) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, ("Test", "Academic", "2021-11-23", False))
    mydb.commit()
    mydb.close()
    assert True

def test_deleteActivity():
    mydb = conn()
    cursor = mydb.cursor()
    sql = "DELETE FROM List_of_Activities WHERE ActivityID = %s"
    cursor.execute(sql, [1])
    mydb.commit()
    mydb.close()
    assert True

def test_markAsComplete():
    mydb = conn()
    cursor = mydb.cursor()
    sql = "UPDATE List_of_Activities SET isDone = TRUE WHERE ActivityID = %s"
    cursor.execute(sql, [1])
    mydb.commit()
    mydb.close()
    assert True

def test_fetchOngoingData():
    mydb = conn()
    cursor = mydb.cursor()
    sql = "SELECT * FROM List_of_Activities WHERE isDone = FALSE"
    cursor.execute(sql)
    result = cursor.fetchall()
    mydb.close()
    assert result

def test_fetchIdleData():
    mydb = conn()
    cursor = mydb.cursor()
    sql = "SELECT * FROM List_of_Activities WHERE isDone = TRUE"
    cursor.execute(sql)
    result = cursor.fetchall()
    mydb.close()
    assert result
