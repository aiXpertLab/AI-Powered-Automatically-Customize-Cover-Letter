# ui_def.py
from tkinter import Button, Canvas

class UIDef:
    def __init__(self, button_callback):
        self.can_small = Canvas()  # Replace this with your actual Canvas creation logic
        self.btn_scrape = Button(self.can_small, text="Click me", cursor='hand2',
                                  activebackground="#5E95FF", borderwidth=0, highlightthickness=0,
                                  relief="flat", command=button_callback)

    def def_hw_window(self, home_instance):
        # Define the window layout or any other logic here
        pass
