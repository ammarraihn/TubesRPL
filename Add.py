from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()

activity = input ("Tambahkan aktivitas: ")
category = input ("Kategori: ")
dl = input ("Deadline (YYYY-MM-DD):" )

sql = "INSERT INTO List_of_Activities (ActivityName, Category, Deadline) VALUES (%s, %s, %s)"
vals = (activity, category, dl)
cursor.execute(sql, vals)
mydb.commit()