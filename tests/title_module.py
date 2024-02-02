import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("100x100")  # Set the initial window size

# Create a frame with a red background
frame = tk.Frame(root, bg='red', width=200, height=200)
frame.pack()

# Create a canvas with a blue background
canvas = tk.Canvas(root, bg='blue', width=300, height=300)
canvas.pack()

# Run the Tkinter event loop
root.mainloop()
