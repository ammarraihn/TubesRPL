from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from userInterface import Dashboard, Completed, Expired


class mainApp(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)

        self.title("OnTrack : To-do Application")
        self.navbar()
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
  
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for Page in (Dashboard, Completed, Expired):
            frame = Page(self.container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Dashboard)


    def navbar(self):   # Navigation bar setiap page

        # HEADER
        self.header = Frame(self, background="#A9A9A9", height=100)
        self.header.pack(fill=X)

        # LOGO ONTRACK
        logo1 = Image.open("logo.png")
        resize_logo1 = logo1.resize((70,70))
        logo_ontrack = ImageTk.PhotoImage(resize_logo1)
        
        label1 = Label(self.header, image=logo_ontrack)
        label1.image = logo_ontrack
        label1.pack(side=LEFT, pady=20, padx=15)
        

        # COMPLETED BUTTON
        completed = Button(self.header, text="Completed", command=lambda: self.show_frame(Completed), padx=20, pady=12)
        completed.pack(side=RIGHT, padx=50)

        # DASHBOARD BUTTON
        completed = Button(self.header, text="Dashboard", command=lambda: self.show_frame(Dashboard), padx=20, pady=12)
        completed.pack(side=RIGHT, padx=50)

        #btn1 = Image.open("home.png")
        #resize_btn1 = btn1.resize((40, 40))
        #home_btn1 = ImageTk.PhotoImage(resize_btn1)
        
        #home = Button(self.header, image=home_btn1, padx=20)
        #home.image = home_btn1 # keep a reference!
        #home.pack(side=RIGHT, padx=50)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

if __name__ == "__main__":
    app = mainApp()
    app.state('zoomed')
    app.mainloop()