from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from manageActivity import addActivity


class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.centralframe = Frame(self, highlightbackground="black", highlightthickness=1)
        self.centralframe.pack(ipady=700, ipadx=700, pady=35)

        self.lbl = Label(self.centralframe, text="DASHBOARD" )
        self.lbl.pack()

        self.ongoingframe = Frame(self.centralframe, highlightbackground="black", highlightthickness=1)
        self.ongoingframe.pack(ipady=170, ipadx=500, pady=18)
        self.idleframe = Frame(self.centralframe, highlightbackground="black", highlightthickness=1)
        self.idleframe.pack(ipady=170, ipadx=500, pady=18)

        self.addbtn = Button(self.centralframe, text="ADD", command = self.popup_window)
        self.addbtn.pack(ipady=15, ipadx=30)
        
        #label1.grid(row = 0, column = 1, padx = 10, pady = 10)

        #self.tree = ttk.Treeview (self, column=("#0", "#1", "#2"))

        #self.tree.column ("#0", width=1000, minwidth=50)
        #self.tree.column ("#1", width=70, minwidth=50)
        #self.tree.column ("#2", width=70, minwidth=50)

        #self.tree.heading ("#0", text="Activity")
        #self.tree.heading ("#1", text="Category")
        #self.tree.heading ("#2", text="Deadline")

        #self.tree.pack()

    def popup_window(self):
        addActivity(self)
        

class Completed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        self.centralframe = Frame(self, highlightbackground="black", highlightthickness=1)
        self.centralframe.pack(ipady=700, ipadx=900, pady=35)

        self.lbl = Label(self.centralframe, text="COMPLETED" )
        self.lbl.pack()

        self.category1frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category1frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category2frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category2frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category3frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category3frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category4frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category4frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)

class Expired(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.centralframe = Frame(self, highlightbackground="black", highlightthickness=1)
        self.centralframe.pack(ipady=700, ipadx=900, pady=35)

        self.lbl = Label(self.centralframe, text="EXPIRED" )
        self.lbl.pack()

        self.category1frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category1frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category2frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category2frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category3frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category3frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)
        self.category4frame = Frame(self.centralframe, highlightbackground="red", highlightthickness=1)
        self.category4frame.pack(padx=20, side=RIGHT, expand=True, fill=BOTH)

