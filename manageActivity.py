from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector


class manageActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def addData(self):
        try:
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
                messagebox.showinfo("Add Activity", "Activity record entered successfully")
        except:
            messagebox.showerror("Add Activity Form", "Error Occured, Please entry valid data")

    def deleteActivity(self):
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        if vals != vals[0] == '' and vals[1] == '':
            messagebox.showerror("Delete Activity", "Please select an activity to delete")
        else:
            mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
            cursor = mydb.cursor()

            ask = messagebox.askyesno("Delete Activity", "Are you sure you want to delete this activity?")
            if ask > 0:
                for val in vals:
                    if (val != ''):
                        sql = "DELETE FROM List_of_Activities WHERE ActivityID = %s"
                        cursor.execute(sql, [val[0]])
                mydb.commit()

                self.parent.fetchOngoingData()
                self.parent.fetchIdleData()
                mydb.close()

                if not (vals[0] == '' and vals[1] == ''):
                    messagebox.showinfo("Delete Activity", "Activity record deleted successfully")

                # Reset selection
                for item in self.parent.ongoing_records.selection():
                    self.parent.ongoing_records.selection_remove(item)

                for item in self.parent.idle_records.selection():
                    self.parent.idle_records.selection_remove(item)
            else:
                messagebox.showinfo("Delete Activity", "Activity record not deleted")

    def markAsComplete(self, ):
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        if vals != vals[0] == '' and vals[1] == '':
            messagebox.showerror("Mark as Complete", "Please select an activity to mark as complete")
        else:
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
                messagebox.showinfo("Mark as Complete", "Congrats, you've completed an activity!")

            # Reset selection
            for item in self.parent.ongoing_records.selection():
                self.parent.ongoing_records.selection_remove(item)

            for item in self.parent.idle_records.selection():
                self.parent.idle_records.selection_remove(item)
            



