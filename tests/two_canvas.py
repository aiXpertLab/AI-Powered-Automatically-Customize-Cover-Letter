# Import required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter window
win = Tk()
win.geometry("1200x850")

# Create an instance of style class
style=ttk.Style(win)

def open_new_win():
   win.geometry("300x50")
   top=Toplevel(win)
   canvas1=Canvas(canvas, height=180, width=100, bg="#aaaffe")
   canvas1.pack()
   Label(canvas1, text="You can modify this text", font='Helvetica 18 bold').pack()

# Create a canvas widget
canvas=Canvas(win, height=400, width=300)
canvas.pack()

# Create a button widget
button=ttk.Button(canvas, text="Open Window", command=open_new_win)
button.pack(pady=30)

win.mainloop()