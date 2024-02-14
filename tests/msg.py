import tkinter as tk
import tkinter.messagebox as msgbox

def test_error_message_box():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Mock the expected values
    error_title = "Error Code 401 - OpenAI Invalid Authentication"
    error_message = ("Quick fix: \n1. Double-check your OpenAI API key.\n2. Set up your key environment.\n3. Try again!")

    msgbox.showerror(title="Error Code 401 - OpenAI Invalid Authentication", message="Quick fix: \n1. Double-check your OpenAI API key.\n2. Set up your key environment.\n3. Try again!")

    # Simulate user closing the message box
    root.destroy()

# Run the test
test_error_message_box()


