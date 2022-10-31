from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()


sql = "SELECT ActivityID, ActivityName, Deadline, CategoryName FROM List_of_Activities INNER JOIN list_of_categories"
cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    print("ActivityID: ", row[0], "| ActivityName: ", row[1], "| Category: ", row[2], "| Deadline: ", row[3])

activityID = input ("Delete: " )
sql = "DELETE FROM List_of_Activities WHERE ActivityID = %s"
vals = [activityID]
cursor.execute(sql, vals)
mydb.commit()