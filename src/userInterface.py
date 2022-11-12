from tkinter import *
from tkinter import ttk
from manageActivity import manageActivity
import tkinter as tk
import mysql.connector

HEADING1 = ('Poppins', 20, 'bold')
HEADING2 = ('Poppins', 14)
FONT = ('Poppins', 12)


class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.activityID = IntVar()
        self.activityName = StringVar()
        self.category = StringVar()
        self.deadline = StringVar()

        self.manageAct =manageActivity(self)

        #================================== Dashboard Frame ==================================

        self.centralframe = Frame(self, background="#1c2e3e")
        self.centralframe.pack(ipady=700, ipadx=700)

        self.lbl = Label(self.centralframe, text="DASHBOARD", font=HEADING1, background="#1c2e3e", borderwidth=0, fg="white")
        self.lbl.pack(anchor="center", pady=55)

        self.contentframe = Frame(self.centralframe, background="#1c2e3e")
        self.contentframe.pack()

        self.tableframe = Frame(self.contentframe, background="#1c2e3e")
        self.tableframe.pack(side=LEFT)

        self.ongoingframe = Frame(self.tableframe)
        self.ongoingframe.pack(ipady=130, ipadx=400)
        self.ongoingframelabel = LabelFrame(self.ongoingframe, text="Task for Today", font=HEADING2, background="#1c2e3e", foreground="#ffffff")
        self.ongoingframelabel.pack(fill=BOTH, expand=YES, ipady=16)
        self.ongoingframe.pack_propagate(False)

        self.idleframe = Frame(self.tableframe)
        self.idleframe.pack(ipady=130, ipadx=400, pady=20)
        self.idleframelabel = LabelFrame(self.idleframe, text="Your Task Later",font=HEADING2, background="#1c2e3e", foreground="#ffffff")
        self.idleframelabel.pack(fill=BOTH, expand=YES, ipady=16)
        self.idleframe.pack_propagate(False)

        self.btnframe = Frame(self.contentframe, background="#1c2e3e")
        self.btnframe.pack(side=LEFT, anchor="n", ipadx=20, ipady=30, pady=200, padx=80)
        
        self.addbtn = Button(self.btnframe, text="Add", command = self.popup_window, borderwidth=0, background="#ffffff", fg="#1c2e3e", font=FONT)
        self.addbtn.pack(ipadx=30,expand=True, fill=BOTH, pady=10)
        self.deletebtn = Button(self.btnframe, text="Delete", command= self.manageAct.deleteActivity, borderwidth=0, background="#ffffff", fg="#1c2e3e", font=FONT)
        self.deletebtn.pack(ipadx=30, expand=True, fill=BOTH, pady=10)
        self.markbtn = Button(self.btnframe, text="Mark Complete", command= self.manageAct.markAsComplete, borderwidth=0, background="#f35c27", fg="#1c2e3e", font=FONT)
        self.markbtn.pack(ipadx=30, expand=True, fill=BOTH, pady=10)
        
        # Treeview styling configuration
        style1 = ttk.Style()
        style1.theme_use('clam')
        style1.configure('Treeview',
            background="#ffffff",
            foreground="#1c2e3e",
            rowheight="20",
            fieldbackground="#ffffff",
            font=FONT
            )
        style1.map('Treeview', background=[('selected', '#33d0e5')])

        style2 = ttk.Style()
        style2.configure('Treeview.Heading',
            background="#1c2e3e",
            foreground="#ffffff",
            rowheight="20",
            font=FONT
            )

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

        self.lbl2 = Label(self.addframe, text="Deadline (YYYY-MM-DD) :", font=FONT)
        self.lbl2.pack(fill='x', expand=True)
        self.txtbox2 = Entry(self.addframe, textvariable=self.deadline)
        self.txtbox2.pack(fill='x', expand=True)
        
        self.btn1 = Button(self.addframe, text="Add", font=FONT, command=self.manageAct.addData)
        self.btn1.pack( pady=10)

    # Clear entry box
    def clearentry(self):
        self.activityName.set("")
        self.category.set("")
        self.deadline.set("")   

    # fetch record ongoing
    def fetchOngoingData(self):
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

        
    # fetch record idle
    def fetchIdleData(self): 
        self.idle_records.delete(*self.idle_records.get_children())# Reset treeviewnya

        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty123", database = "ontrack", auth_plugin = "mysql_native_password")
        cursor = mydb.cursor()
        cursor.execute("SELECT ActivityID, ActivityName, CategoryName, Deadline FROM List_of_Activities WHERE Deadline > CURDATE() AND isDone = FALSE ORDER BY Deadline ASC")
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
        tk.Frame.__init__(self, parent, background="#1c2e3e")
        self.controller = controller

        
        #===================== Completed Frame =====================

        self.centralframe = Frame(self, background="#1c2e3e")
        self.centralframe.pack(ipady=700, ipadx=700, pady=35)

        self.lbl = Label(self.centralframe, text="COMPLETED", font=HEADING1, background="#1c2e3e", borderwidth=0, fg="white")
        self.lbl.pack(anchor="n", pady=20)

        self.categorycentralframe = Frame(self.centralframe, background="#1c2e3e")
        self.categorycentralframe.pack(ipadx=600, ipady=10, pady=40)

        # ACADEMIC FRAME
        self.category1frame = Frame(self.categorycentralframe, background="#1c2e3e")
        self.category1frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category1frame.pack_propagate(False)

        self.category1frametitle = Label(self.category1frame, text="Academic", font=HEADING2, background="#1c2e3e", foreground="#ffffff")
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
        self.category2frame = Frame(self.categorycentralframe, background="#1c2e3e")
        self.category2frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category2frame.pack_propagate(False)

        self.category2frametitle = Label(self.category2frame, text="Entertainment", font=HEADING2, background="#1c2e3e", foreground="#ffffff")
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
        self.category3frame = Frame(self.categorycentralframe, background="#1c2e3e")
        self.category3frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category3frame.pack_propagate(False)

        self.category3frametitle = Label(self.category3frame, text="Social", font=HEADING2, background="#1c2e3e", foreground="#ffffff")
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
        self.category4frame = Frame(self.categorycentralframe, background="#1c2e3e")
        self.category4frame.pack(padx=20, side=LEFT, expand=True, fill=X, ipady=250)
        self.category4frame.pack_propagate(False)

        self.category4frametitle = Label(self.category4frame, text="Others", font=HEADING2, background="#1c2e3e", foreground="#ffffff")
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
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Academic' AND isDone = TRUE ORDER BY Deadline ASC")
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
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Entertainment' AND isDone = TRUE ORDER BY Deadline ASC")
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
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Social' AND isDone = TRUE ORDER BY Deadline ASC")
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
        cursor.execute("SELECT ActivityName, Deadline FROM List_of_Activities WHERE CategoryName = 'Others' AND isDone = TRUE ORDER BY Deadline ASC")
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
    