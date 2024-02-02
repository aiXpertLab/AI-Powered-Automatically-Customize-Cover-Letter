# ui_def.py
from tkinter import Button, Canvas

class UIDef:
    def __init__(self, button_callback):
        self.can_small = Canvas()  # Replace this with your actual Canvas creation logic
        self.btn_scrape = Button(self.can_small, text="Click me", command=button_callback)

    def def_hw_window(self, home_instance):
        self.can_small.pack()        # Pack the canvas
        self.btn_scrape.pack(side="top")  # Pack the button

