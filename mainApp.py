from tkinter import *
from PIL import Image, ImageTk
from userInterface import Dashboard, Completed
import tkinter as tk


class mainApp(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)

        self.title("OnTrack : To-do Application")
        self.iconphoto(True, tk.PhotoImage(file='logo_window.png'))
        self.navbar()
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
  
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for Page in (Dashboard, Completed):
            frame = Page(self.container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Dashboard)


    def navbar(self):   # Navigation bar setiap page

        # HEADER
        self.header = Frame(self, background="white", height=100)
        self.header.pack(fill=X)

        # LOGO ONTRACK
        logo1 = Image.open("logo.png")
        resize_logo1 = logo1.resize((250,70))
        logo_ontrack = ImageTk.PhotoImage(resize_logo1)
        
        label1 = Label(self.header, image=logo_ontrack, borderwidth=0)
        label1.image = logo_ontrack
        label1.pack(side=LEFT, pady=20, padx=15)
        

        # COMPLETED BUTTON
        completed = Button(self.header, text="Completed", command=lambda: self.show_frame(Completed), padx=20, pady=12, font=('Poppins', 14), borderwidth=0, background="#1c2e3e", fg="white")
        completed.pack(side=RIGHT, padx=50)

        # DASHBOARD BUTTON
        completed = Button(self.header, text="Dashboard", command=lambda: self.show_frame(Dashboard), padx=20, pady=12, font=('Poppins', 14), borderwidth=0, background="#1c2e3e", fg="white")
        completed.pack(side=RIGHT, padx=50)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.refetchData()
        frame.tkraise()
        

if __name__ == "__main__":
    app = mainApp()
    app.state('zoomed')
    app.mainloop()