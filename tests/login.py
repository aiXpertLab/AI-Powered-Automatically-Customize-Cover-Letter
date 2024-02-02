# login.py
from tests.onewindow.homewindow import HomeWindow

class LoginCanvas:
    def __init__(self):
        # Access the mainwindow object through HomeWindow
        self.mainwindow = HomeWindow().get_mainwindow()

    def some_method_using_mainwindow(self):
        # Access the mainwindow object and do something with it
        print(f"Using mainwindow: {self.mainwindow}")