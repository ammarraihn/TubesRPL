from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()

sql = "SELECT * FROM List_of_Activities"
cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    print("ActivityID: ", row[0], "| ActivityName: ", row[1], "| Category: ", row[2], "| Deadline: ", row[3])