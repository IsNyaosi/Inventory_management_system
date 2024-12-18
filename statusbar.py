from tkinter import *
from PIL import ImageTK, Image     #pil is a image module

root = Tk()
root.title('Bush.com Image Viewer')
root.iconbitmap('c:/gui/mayback.jpg')

my_img1 = ImageTK.PhotoImage(Image.open())
my_img2 = ImageTK.PhotoImage(Image.open())
my_img3 = ImageTK.PhotoImage(Image.open())
my_img4 = ImageTK.PhotoImage(Image.open())
my_img5 = ImageTK.PhotoImage(Image.open())

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = Label(root, text='Image 1 of 5')

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forwrd(image_number):
    global my_labe
    global  button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])