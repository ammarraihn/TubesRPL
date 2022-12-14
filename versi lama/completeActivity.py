from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()


sql = "SELECT ActivityID, ActivityName, Deadline, CategoryName FROM List_of_Activities INNER JOIN list_of_categories WHERE isDone = FALSE"
cursor.execute(sql)
data = cursor.fetchall()

for row in data:
    print("ActivityID: ", row[0], "| ActivityName: ", row[1], "| Category: ", row[2], "| Deadline: ", row[3])


sql = "UPDATE List_of_Activities SET isDone = TRUE WHERE ActivityID = %s"
activityID = input ("Mark As Done: " )
vals = [activityID]
cursor.execute(sql, vals)
mydb.commit()