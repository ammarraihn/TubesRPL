from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()

# ONGOING ACTIVITY
sql = "SELECT ActivityID, ActivityName, Deadline, CategoryName FROM List_of_Activities INNER JOIN list_of_categories WHERE Deadline = CURDATE() AND isDone = FALSE"
cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    print("ActivityID: ", row[0], "| ActivityName: ", row[1], "| Deadline: ", row[2], "| Category: ", row[3])

print("IDLE")
# IDLE ACTIVITY
sql = "SELECT ActivityID, ActivityName, Deadline, CategoryName FROM List_of_Activities INNER JOIN list_of_categories WHERE Deadline > CURDATE() AND isDone = FALSE"
cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    print("ActivityID: ", row[0], "| ActivityName: ", row[1], "| Deadline: ", row[2], "| Category: ", row[3])