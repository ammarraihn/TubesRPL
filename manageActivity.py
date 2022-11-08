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
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()

        # Bisa ngedelete dari salah satu ongoing atau idle tree, atau bisa delete dari keduanya langsung
        for val in vals:
            if (val != ''):
                sql = "DELETE FROM List_of_Activities WHERE ActivityID = %s"
                cursor.execute(sql, [val[0]])
        mydb.commit()

        self.parent.fetchOngoingData()
        self.parent.fetchIdleData()
        mydb.close()

        if not (vals[0] == '' and vals[1] == ''):
            messagebox.showinfo("Delete", "Record Deleted Successfully")

        # Reset selection
        for item in self.parent.ongoing_records.selection():
            self.parent.ongoing_records.selection_remove(item)

        for item in self.parent.idle_records.selection():
            self.parent.idle_records.selection_remove(item)

    def markAsComplete(self, ):
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()

        # Bisa ngecomplete dari salah satu ongoing atau idle tree, atau bisa complete dari keduanya langsung
        for val in vals:
            if (val != ''):
                sql = "UPDATE List_of_Activities SET isDone = TRUE WHERE ActivityID = %s"
                cursor.execute(sql, [val[0]])
        mydb.commit()

        self.parent.fetchOngoingData()
        self.parent.fetchIdleData()
        mydb.close()

        if not (vals[0] == '' and vals[1] == ''):
            messagebox.showinfo("Add Activity Form", "Activity Record Entered Successfully")

        # Reset selection
        for item in self.parent.ongoing_records.selection():
            self.parent.ongoing_records.selection_remove(item)

        for item in self.parent.idle_records.selection():
            self.parent.idle_records.selection_remove(item)
            



