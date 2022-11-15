import pytest
import mysql.connector
from modelActivity import modelActivity
from datetime import date, timedelta

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

# Memasukkan aktivitas yang memiliki deadline hari ini dan mengetes apakah yang dimasukkan ada dan sesuai
def test_add_and_select_ongoing():
    modelAct = modelActivity()
    modelAct.addToDb("c20234c4-b428-4df8-93f6-6971dd8ffb49", "Academic", str(date.today()))
    ongoing = modelAct.selectOngoingDb()
    for item in ongoing:
        if (item[1] == "c20234c4-b428-4df8-93f6-6971dd8ffb49"):
            aktivitas = item
            break
    isCorrect = ((aktivitas[1] == "c20234c4-b428-4df8-93f6-6971dd8ffb49") and 
                (aktivitas[2] == "Academic") and 
                (str(aktivitas[3]) == str(date.today())))
    assert isCorrect

# Memasukkan aktivitas yang memiliki deadline besok dan mengetes apakah yang dimasukkan ada dan sesuai
def test_add_and_select_idle():
    modelAct = modelActivity()
    modelAct.addToDb("8b6bdab2-973d-4ba4-b9fb-9937d23ea0f6", "Academic", str(date.today()+ timedelta(days=1)))
    idle = modelAct.selectIdleDb()
    for item in idle:
        if (item[1] == "8b6bdab2-973d-4ba4-b9fb-9937d23ea0f6"):
            aktivitas = item
            break

    
    isCorrect = ((aktivitas[1] == "8b6bdab2-973d-4ba4-b9fb-9937d23ea0f6") and 
                (aktivitas[2] == "Academic") and 
                (str(aktivitas[3]) == str(date.today()+ timedelta(days=1))))
    assert isCorrect

# Melakukan mark complete kepada aktivitas dan mengecek apakah aktivitas tersebut ada di completed yang dicari berdasarkan kategori
def test_complete_and_select_completed():
    modelAct = modelActivity()
    ongoing = modelAct.selectOngoingDb()
    for item in ongoing:
        if (item[1] == "c20234c4-b428-4df8-93f6-6971dd8ffb49"):
            aktivitas = item
            break
    modelAct.completeInDb([aktivitas])

    completed = modelAct.selectCompletedByCategoryDb("Academic")
    completedAktivitas = None
    for item in completed:
        if (item[0] == aktivitas[1]): # item[0] dan aktivitas[1] adalah nama aktivitas
            completedAktivitas = item
            break

    print(completedAktivitas)

    # ngecek apakah yang udah dimark as complete ada di completed atau tidak
    isCorrect = ((completedAktivitas[0] == "c20234c4-b428-4df8-93f6-6971dd8ffb49") and 
                (aktivitas[2] == "Academic"))

    assert isCorrect 

# Menghapus aktivitas dan mengetes apakah benar terhapus atau tidak
def test_delete_activity():
    modelAct = modelActivity()
    idle = modelAct.selectIdleDb()
    aktivitas = []
    for item in idle:
        if (item[1] == "8b6bdab2-973d-4ba4-b9fb-9937d23ea0f6"):
            aktivitas.append(item)
    modelAct.delInDb(aktivitas)

    idle = modelAct.selectIdleDb()
    isAktivitasDoesntExist = True
    for item in idle:
        if (item[1] == "8b6bdab2-973d-4ba4-b9fb-9937d23ea0f6"):
            isAktivitasDoesntExist = False # Jika ketemu berarti aktivitas tidak berhasil terhapus
            break

    assert isAktivitasDoesntExist

# Untuk bersih bersih aktivitas dummy yang dimasukkin pas test 
def test_delete_remaining():
    mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
    cursor = mydb.cursor()

    sql = "DELETE FROM List_of_Activities WHERE ActivityName = %s"
    cursor.execute(sql, ["c20234c4-b428-4df8-93f6-6971dd8ffb49"])
    mydb.commit()
    mydb.close()
