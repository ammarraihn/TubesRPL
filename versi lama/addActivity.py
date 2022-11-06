from database_connect import database_connect

mydb = database_connect()
cursor = mydb.cursor()

# Proses input nilai
activity = input ("Tambahkan aktivitas: ")

# Mengambil kategori yang ada
sql = "SELECT * FROM List_of_categories"
cursor.execute(sql)
data = cursor.fetchall()
categorySet = set()
for row in data:
    print(row[0], " ", row[1])
    categorySet.add(row[0])

category = int(input("Pilih kategori: "))

while category not in categorySet:
    print("Kategori yang dipilih tidak valid")
    category = int(input ("Pilih kategori:"))

dl = input ("Deadline (YYYY-MM-DD):" )

# Memasukkan ke database
sql = "INSERT INTO List_of_Activities (ActivityName, CategoryID, Deadline, isDone) VALUES (%s, %s, %s, FALSE)"
vals = (activity, category, dl)
cursor.execute(sql, vals)
mydb.commit()