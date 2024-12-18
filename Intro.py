'''
    INVENTORY MANAGEMENT SYSTEM
    Nyaosi Brian
'''
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
      self.splashminw=Tk()
      self.splashminw.title("About")
      width = 1000
      height = 700
      self.splashminw.config(bg="#4267b2")
      screen_width = self.splashminw.winfo_screenwidth()
      screen_height = self.splashminw.winfo_screenheight()
      x = (screen_width / 2) - (width / 2)
      y = (screen_height / 2) - (height / 2)
      self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
      self.splashminw.resizable(0,0)
      path = "images/tools.jpg"
      img = ImageTk.PhotoImage(Image.open(path))
      main=LabelFrame(self.splashminw, width=890, height=560,bg="snow",relief="sunken")
      main.place(x=55,y=70)
      photoframe = LabelFrame(main, width=420, height=444, bg="snow", relief="raised")
      pic=Label(photoframe, image=img)
      pic.place(x=6, y=6)
      photoframe.place(x=10, y=100)
      Label(main, text="WAGA SPARE PARTS INVENTORY SYSTEM",font="roboto 30 bold underline",bg="snow").place(x=25, y=10)
      Label(main, text="NYAOSI BRIAN",font="roboto 32 bold",bg="snow").place(x=450, y=160)
      Label(main, text="Reg. No.  I39/1893/2018",font="roboto 16 bold",bg="snow").place(x=445+5, y=260)
     
      Label(main, text="Email:  bushjr099@gmail.com",font="roboto 16 bold",bg="snow").place(x=445+5, y=360)
      Label(main, text="Phone no.  +254745958319",font="roboto 16 bold",bg="snow").place(x=445+5, y=410)
      pic.bind('<Motion>', lambda event: self.splashminw.destroy())
     # self.splashminw.after(10000,lambda :self.splashminw.destroy())
      self.splashminw.mainloop()


