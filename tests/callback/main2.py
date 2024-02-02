# main.py
import tkinter as tk
from ui_def import UIDef

class Home(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ui = UIDef(self.button_click)
        self.ui.def_hw_window(self)

    def button_click(self):
        # Your button click event handler logic here
        print("Button clicked in Home!")

if __name__ == "__main__":
    home = Home()
    home.mainloop()
