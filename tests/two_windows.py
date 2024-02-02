from tkinter import *
class NextWindow:
 
   def __init__(self, master):
       self.master = master
       master.title('Next') 
 
       self.button = Button(master, text = 'Close', 
                            command = master.destroy)
       self.button.pack()
class StartWindow:
 
   def __init__(self, master):
      self.master = master
      master.title('Start')
 
      self.button = Button(master, text = 'Open', 
                           command = self.openNext)
      self.button.pack()
 
   def openNext(self):
      self.newWindow = Toplevel(self.master)
      self.app = NextWindow(self.newWindow)
# main program #
root = Tk()
app = StartWindow(root)
root.mainloop()