from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


class addActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.popup = Toplevel(self)

        self.popup.title("Add Your Activity to Keep Your Productivity")
        self.popup.geometry("500x500")

        """ self.lbl1 = Label(self.popup, text="Activity")
        self.lbl1.pack()
        self.txtbox1 = Entry(self.popup)
        self.txtbox1.pack()

        self.lbl2 = Label(self.popup, text="Category")
        self.lbl2.pack()
        self.txtbox2 = Entry(self.popup)
        self.txtbox2.pack() """
    
        self.lbl1 = Label(self.popup, text="Activity")
        self.lbl1.grid(row=0, column=0)
        self.txtbox1 = Entry(self.popup)
        self.txtbox1.grid(row=0, column=1)

        self.lbl2 = Label(self.popup, text="Category")
        self.lbl2.grid(row=1, column=0)
        self.listbox1 = ttk.Combobox(self.popup, values=["Kuliah", "Main", "Lainnya"])
        self.listbox1.grid(row=1, column=1)

        self.lbl2 = Label(self.popup, text="Deadline")
        self.lbl2.grid(row=2, column=0)
        self.txtbox2 = Entry(self.popup)
        self.txtbox2.grid(row=2, column=1)

        self.btn1 = Button(self.popup, text="Add")
        self.btn1.grid(column=0, row=3, columnspan=3)

    
class deleteActivity():
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


class markAsComplete():
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

