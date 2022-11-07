from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from sqlite3 import Cursor
import mysql.connector


class manageActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def addData(self):
        if self.parent.activityName.get() == "" or self.parent.category.get() == "" or self.parent.deadline.get() == "":
            messagebox.showerror("Add Activity Form", "You must enter all details")
        else:
            mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
            cursor = mydb.cursor()
            cursor.execute("INSERT INTO List_of_Activities (ActivityName, CategoryName, Deadline, isDone) VALUES ('{}', '{}', '{}', FALSE)".format(
                self.parent.activityName.get(), 
                self.parent.category.get(), 
                self.parent.deadline.get()
            ))
            mydb.commit()
            mydb.close()
            self.parent.fetchOngoingData()
            self.parent.fetchIdleData()
            messagebox.showinfo("Add Activity Form", "Activity Record Entered Succsessfully")

    def deleteActivity(self):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM List_of_Activities WHERE ActivityName = %s", self.parent.activityName.get())
        
        mydb.commit()
        mydb.close()
        self.parent.fetchOngoingData()
        messagebox.showinfo("Add Activity Form", "Activity Record Entered Succsessfully")

    def markAsComplete(self):
        pass
            



