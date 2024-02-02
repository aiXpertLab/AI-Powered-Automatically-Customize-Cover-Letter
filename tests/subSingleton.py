import tkinter as tk
from tkinter import scrolledtext

class YourApp:
    def __init__(self):
        # Create a Tkinter window
        self.root = tk.Tk()

        # Create a ScrolledText widget
        self.working_text = scrolledtext.ScrolledText(self.root, height=10, width=40, wrap=tk.WORD)
        self.working_text.pack()

        # Add some text to the ScrolledText widget for testing
        sample_text = "This is some sample text. " * 10
        self.working_text.insert(tk.END, sample_text)

        # Start the Tkinter event loop
        self.root.mainloop()

# Create an instance of the app
app = YourApp()
