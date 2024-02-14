import os, shutil, json, random, inspect
import tkinter as tk
import openai

from openai import OpenAI
from config.config import Path_
from tkinter import filedialog, CURRENT

class RandomTitleGenerator:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_random_line(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return random.choice(lines).strip()       

class ObjPrinter:
    @staticmethod
    def print_obj(obj):
        # Print the object, its type, and the class hierarchy
        # ObjPrinter.print_obj(ologcan)

        print("Object:", obj)
        print("Type:", type(obj))
        print("Class Hierarchy:")
        for cls in type(obj).__mro__:
            print(f"  - {cls.__name__} ({cls.__module__})")

        print("\nInstance Variables:")
        for key, value in vars(obj).items():
            print(f"  - {key}: {value}")

class ShowJson:
    @staticmethod
    def show_json(obj):
        print(json.loads(obj.model_dump_json()))

class KeyGood:
    @staticmethod

    def check_key(apikey="None"):
        print(apikey)
        windows_key = os.environ.get("OPENAI_API_KEY")
        if windows_key is not None:
            try:
                client=OpenAI()
                client.models.list()
                return client
            except Exception as e:
                client = OpenAI(api_key = apikey)
                try:
                    client.models.list()
                    print('good')
                    return client
                except Exception as e:
                    return None
        else:
            client = OpenAI(api_key = apikey)
            try:
                client.models.list()
                print('good')
                return client
            except Exception as e:
                return None
        
class CheckKeyInComputer:
    @staticmethod
    def check_key_in_computer():
        windows_key = os.environ.get("OPENAI_API_KEY")
        if windows_key is None:
            return False
        print(f'key in env is good:  {client.api_key[:9]}')
        return True
        


class CopyResume:
    @staticmethod
    def copy_and_rename_file():
        data_path = Path_.DATA_PATH
        myfile_ = data_path / "MyFile.pdf"

        if myfile_.exists():
            print(f"{myfile_} existed.")
            return "existed"
        else:
            # Ask the user to locate their original file
            original_file_path = filedialog.askopenfilename(title="Locate and click your resume: ")

            if original_file_path:
                try:
                    # Create the destination folder if it doesn't exist
                    if not data_path:
                        os.makedirs(data_path)

                    # Copy the original file to the destination folder with the new filename
                    shutil.copy2(original_file_path, myfile_)
                    print(f"File copied to {myfile_}")
                    return "succeed"
                except Exception as e:
                    print(f"Error copying file: {e}")        
                    return "failed"

class HyperlinkManager:

    def __init__(self, text):

        self.text = text

        self.text.tag_config("hyper", foreground="#5E95FF", underline=1)

        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)

        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return
        

class ExceptionHandler:
    @staticmethod
    def handle_exception(exception, additional_info=None):
        frame = inspect.currentframe()
        module_name = inspect.getmodule(frame).__name__
        function_name = frame.f_code.co_name
        line_number = frame.f_lineno
        globals_dict = frame.f_globals

        # Handle the exception
        print(f"Exception occurred:")
        if additional_info:
            print(f"  - Additional Info: {additional_info}")
        print(f"  - Module: {module_name}")
        print(f"  - Function: {function_name}")
        print(f"  - Line: {line_number}")
        # print(f"  - Globals: {globals_dict}")
        print(f"  - Exception Type: {type(exception).__name__}")
        print(f"  - Exception Details: {exception}")

class ChangeText:
    @staticmethod
    def bold_text(text_widget, keyword):
        text_widget.tag_configure("bold",   font=("Montserrat", 14 * -1, "bold"))

        start_index = "1.0"
        while True:
            start_index = text_widget.search(keyword, start_index, stopindex=tk.END)
            if not start_index: break

            # Calculate the end index of the keyword
            end_index = f"{start_index}+{len(keyword)}c"

            # Apply the "bold" tag to the keyword
            text_widget.tag_add("bold", start_index, end_index)

            # Move the start_index to the next occurrence
            start_index = end_index


    @staticmethod
    def color_line(text_widget, line_number, color):
        # Create a tag configuration for colored text
        text_widget.tag_configure(color, foreground=color)

        # Get the start and end indices of the specified line
        start_index = f"{line_number}.0"
        end_index = f"{line_number + 1}.0"

        # Apply the color tag to the specified line
        text_widget.tag_add(color, start_index, end_index)