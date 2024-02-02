import tkinter as tk

class MultiCanvasWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Canvas Window")

        self.current_canvas = None
        self.create_canvas("Canvas 1")  # Create the initial canvas

        # Button to switch to the next canvas
        switch_button = tk.Button(root, text="Switch Canvas", command=self.switch_canvas)
        switch_button.pack(pady=10)

    def create_canvas(self, canvas_name):
        # Destroy the current canvas if it exists
        if self.current_canvas:
            self.current_canvas.destroy()

        # Create a new canvas
        self.current_canvas = tk.Canvas(self.root, width=300, height=200, bg="white")
        self.current_canvas.pack()

        # Add content to the canvas (example: display canvas name)
        self.current_canvas.create_text(150, 100, text=canvas_name, font=("Helvetica", 14))

    def switch_canvas(self):
        # Example: switch to a different canvas (you can customize this logic)
        canvas_number = int(self.current_canvas.cget("text").split()[-1]) + 1
        new_canvas_name = f"Canvas {canvas_number}"
        self.create_canvas(new_canvas_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiCanvasWindow(root)
    root.mainloop()
