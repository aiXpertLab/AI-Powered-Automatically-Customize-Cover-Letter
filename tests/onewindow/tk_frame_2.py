import tkinter as tk
from tkinter import ttk
from tk_frame_2_sub import MainPage, SidePage, CompletionScreen
# Allowing us to extend from the Tk class
# class testClass(tk.Tk):

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adding a title to the window
        self.wm_title("Test Application")
        self.geometry("1012x506")
        self.configure(bg="#5E95FF")


        # Frame
        container = tk.Frame(self, height=100, width=100)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()