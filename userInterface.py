from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from manageActivity import manageActivity
from sqlite3 import Cursor
import mysql.connector

HEADING1 = ('Perpetua', 20, 'bold')
HEADING2 = ('Perpetua', 14)
FONT = ('Perpetua', 12)


class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.activityID = IntVar()
        self.activityName = StringVar()
        self.category = StringVar()
        self.deadline = StringVar()

        self.manageAct =manageActivity(self)

        self.centralframe = Frame(self, highlightbackground="black", highlightthickness=1)
        self.centralframe.pack(ipady=700, ipadx=700)

        self.lbl = Label(self.centralframe, text="DASHBOARD", font=HEADING1)
        self.lbl.pack(anchor="center", pady=20)

        self.ongoingframe = Frame(self.centralframe, highlightbackground="black", highlightthickness=1)
        self.ongoingframe.pack(ipady=130, ipadx=400)
        self.ongoingframelabel = LabelFrame(self.ongoingframe, text="Task for Today", font=HEADING2)
        self.ongoingframelabel.pack(fill=BOTH, expand=YES)
        self.ongoingframe.pack_propagate(False)

        self.idleframe = Frame(self.centralframe, highlightbackground="black", highlightthickness=1)
        self.idleframe.pack(ipady=130, ipadx=400, pady=20)
        self.idleframelabel = LabelFrame(self.idleframe, text="Your Task Later",font=HEADING2)
        self.idleframelabel.pack(fill=BOTH, expand=YES)
        self.idleframe.pack_propagate(False)

        self.btnframe = Frame(self.centralframe, highlightbackground="black", highlightthickness=1)
        self.btnframe.pack(ipadx=70, ipady=20)
        
        self.addbtn = Button(self.btnframe, text="Add", command = self.popup_window)
        self.addbtn.pack(ipadx=30, side=LEFT, expand=True, fill=BOTH)
        self.deletebtn = Button(self.btnframe, text="Delete", command= self.manageAct.deleteActivity)
        self.deletebtn.pack(ipadx=30, side=LEFT, expand=True, fill=BOTH)
        self.markbtn = Button(self.btnframe, text="Mark Complete", command= self.manageAct.markAsComplete)
        self.markbtn.pack(ipadx=30, side=LEFT, expand=True, fill=BOTH)
        
        # Table OnGoing Activity
        scroll_y_ongoing = Scrollbar(self.ongoingframe, orient=VERTICAL)
        self.ongoing_records = ttk.Treeview (self.ongoingframe, height=10, columns=("ActivityID", "Activity", "Category", "Deadline"), yscrollcommand= scroll_y_ongoing)
        scroll_y_ongoing.pack(side="right", fill=Y)

        self.ongoing_records["displaycolumns"]=("Activity", "Category", "Deadline")

        self.ongoing_records.heading("Activity", text="Activity")
        self.ongoing_records.heading("Category", text="Category")
        self.ongoing_records.heading("Deadline", text="Deadline")

        self.ongoing_records['show'] = 'headings'

        self.ongoing_records.column("Activity", width=30)
        self.ongoing_records.column("Category", width=30)
        self.ongoing_records.column("Deadline", width=30)

        self.ongoing_records.pack(fill=BOTH, expand=1)

        self.fetchOngoingData()

        # Table Idle Activity
        scroll_y_ongoing = Scrollbar(self.idleframe, orient=VERTICAL)
        self.idle_records = ttk.Treeview (self.idleframe, height=10, columns=("ActivityID", "Activity", "Category", "Deadline"), yscrollcommand= scroll_y_ongoing)
        scroll_y_ongoing.pack(side="right", fill=Y)

        self.idle_records["displaycolumns"]=("Activity", "Category", "Deadline")

        self.idle_records.heading("Activity", text="Activity")
        self.idle_records.heading("Category", text="Category")
        self.idle_records.heading("Deadline", text="Deadline")

        self.idle_records['show'] = 'headings'

        self.idle_records.column("Activity", width=30)
        self.idle_records.column("Category", width=30)
        self.idle_records.column("Deadline", width=30)

        self.idle_records.pack(fill=BOTH, expand=1)

        self.fetchIdleData()

    def popup_window(self):    # Add Activity Pop Up


        self.popup = Toplevel(self)

        self.popup.title("Add Your Activity to Keep Your Productivity")
        self.popup.geometry("350x420")

        self.addframe = Frame(self.popup)
        self.addframe.pack(ipadx=50, ipady=50, pady=50)
    
        self.lbl1 = Label(self.addframe, text="Activity :", font= FONT)
        self.lbl1.pack(fill='x', expand=True)
        self.txtbox1 = Entry(self.addframe, textvariable=self.activityName)
        self.txtbox1.pack(fill='x', expand=True)

        self.lbl2 = Label(self.addframe, text="Category :", font=FONT)
        self.lbl2.pack(fill='x', expand=True)
        self.listbox1 = ttk.Combobox(self.addframe, values=["Academic", "Entertainment", "Social", "Others"], textvariable = self.category)
        self.listbox1.pack(fill='x', expand=True)

        self.lbl2 = Label(self.addframe, text="Deadline (YYYY-MM-DD :", font=FONT)
        self.lbl2.pack(fill='x', expand=True)
        self.txtbox2 = Entry(self.addframe, textvariable=self.deadline)
        self.txtbox2.pack(fill='x', expand=True)
        
        self.btn1 = Button(self.addframe, text="Add", font=FONT, command=self.manageAct.addData)
        self.btn1.pack( pady=10)

    def fetchOngoingData(self): # fetch record ongoing
        self.ongoing_records.delete(*self.ongoing_records.get_children()) # Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityID, ActivityName, CategoryName, Deadline FROM List_of_Activities WHERE Deadline = CURDATE() AND isDone = FALSE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.ongoing_records.delete(*self.ongoing_records.get_children())
            for row in result:
                self.ongoing_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def fetchIdleData(self): # fetch record idle
        self.idle_records.delete(*self.idle_records.get_children())# Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityID, ActivityName, CategoryName, Deadline FROM List_of_Activities WHERE Deadline > CURDATE() AND isDone = FALSE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.idle_records.delete(*self.idle_records.get_children())
            for row in result:
                self.idle_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def refetchData(self):
        self.fetchOngoingData()
        self.fetchIdleData()
        

class Completed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        self.centralframe = Frame(self)
        self.centralframe.pack(ipady=700, ipadx=700, pady=35)

        self.lbl = Label(self.centralframe, text="COMPLETED", font=HEADING1)
        self.lbl.pack(anchor="center", pady=20)


        # ACADEMIC FRAME
        self.category1frame = Frame(self.centralframe)
        self.category1frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category1frame.pack_propagate(False)

        self.category1frametitle = Label(self.category1frame, text="Academic", font=HEADING2)
        self.category1frametitle.pack(anchor="center", pady=20)

        scroll_y_category1 = Scrollbar(self.category1frame, orient=VERTICAL)
        self.category1_records = ttk.Treeview (self.category1frame, height=10, columns=("Activity", "Deadline"), yscrollcommand = scroll_y_category1)
        scroll_y_category1.pack(side="right", fill=Y)

        self.category1_records.heading("Activity", text="Activity")
        self.category1_records.heading("Deadline", text="Deadline")

        self.category1_records['show'] = 'headings'

        self.category1_records.column("Activity", width=30)
        self.category1_records.column("Deadline", width=30)

        self.category1_records.pack(fill=BOTH, expand=1)

        self.fetchCategory1Data()

        # ENTERTAINMENT FRAME
        self.category2frame = Frame(self.centralframe)
        self.category2frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category2frame.pack_propagate(False)

        self.category2frametitle = Label(self.category2frame, text="Entertainment", font=HEADING2)
        self.category2frametitle.pack(anchor="center", pady=20)

        scroll_y_category2 = Scrollbar(self.category2frame, orient=VERTICAL)
        self.category2_records = ttk.Treeview (self.category2frame, height=10, columns=("Activity", "Deadline"), yscrollcommand = scroll_y_category2)
        scroll_y_category2.pack(side="right", fill=Y)

        self.category2_records.heading("Activity", text="Activity")
        self.category2_records.heading("Deadline", text="Deadline")

        self.category2_records['show'] = 'headings'

        self.category2_records.column("Activity", width=30)
        self.category2_records.column("Deadline", width=30)

        self.category2_records.pack(fill=BOTH, expand=1)

        self.fetchCategory2Data()

        # SOCIAL FRAME
        self.category3frame = Frame(self.centralframe)
        self.category3frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category3frame.pack_propagate(False)

        self.category3frametitle = Label(self.category3frame, text="Social", font=HEADING2)
        self.category3frametitle.pack(anchor="center", pady=20)

        scroll_y_category3 = Scrollbar(self.category3frame, orient=VERTICAL)
        self.category3_records = ttk.Treeview (self.category3frame, height=10, columns=("Activity", "Deadline"), yscrollcommand = scroll_y_category3)
        scroll_y_category3.pack(side="right", fill=Y)

        self.category3_records.heading("Activity", text="Activity")
        self.category3_records.heading("Deadline", text="Deadline")

        self.category3_records['show'] = 'headings'

        self.category3_records.column("Activity", width=30)
        self.category3_records.column("Deadline", width=30)

        self.category3_records.pack(fill=BOTH, expand=1)

        self.fetchCategory3Data()

        # OTHERs FRAME
        self.category4frame = Frame(self.centralframe)
        self.category4frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category4frame.pack_propagate(False)

        self.category4frametitle = Label(self.category4frame, text="Others", font=HEADING2)
        self.category4frametitle.pack(anchor="center", pady=20)

        scroll_y_category4 = Scrollbar(self.category4frame, orient=VERTICAL)
        self.category4_records = ttk.Treeview (self.category4frame, height=10, columns=("Activity", "Deadline"), yscrollcommand = scroll_y_category4)
        scroll_y_category4.pack(side="right", fill=Y)

        self.category4_records.heading("Activity", text="Activity")
        self.category4_records.heading("Deadline", text="Deadline")

        self.category4_records['show'] = 'headings'

        self.category4_records.column("Activity", width=30)
        self.category4_records.column("Deadline", width=30)

        self.category4_records.pack(fill=BOTH, expand=1)

        self.fetchCategory4Data()

    def fetchCategory1Data(self):
        self.category1_records.delete(*self.category1_records.get_children()) # Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Academic' AND isDone = TRUE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.category1_records.delete(*self.category1_records.get_children())
            for row in result:
                self.category1_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def fetchCategory2Data(self):
        self.category2_records.delete(*self.category2_records.get_children()) # Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Entertainment' AND isDone = TRUE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.category2_records.delete(*self.category2_records.get_children())
            for row in result:
                self.category2_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def fetchCategory3Data(self):
        self.category3_records.delete(*self.category3_records.get_children()) # Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Social' AND isDone = TRUE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.category3_records.delete(*self.category3_records.get_children())
            for row in result:
                self.category3_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def fetchCategory4Data(self):
        self.category4_records.delete(*self.category4_records.get_children()) # Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Others' AND isDone = TRUE")
        result = cursor.fetchall()
        if len(result) != 0:
            self.category4_records.delete(*self.category4_records.get_children())
            for row in result:
                self.category4_records.insert('', END, values= row)
            mydb.commit()
        mydb.close()

    def refetchData(self):
        self.fetchCategory1Data()
        self.fetchCategory2Data()
        self.fetchCategory3Data()
        self.fetchCategory4Data()
    