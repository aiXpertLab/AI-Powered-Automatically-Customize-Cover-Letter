import os, sys
from pathlib import Path
from dotenv import load_dotenv

# print(__name__)
# print(sys.path[0])
# print('---------------')

class Path_:
    ROOT_PATH   = Path(__file__).resolve().parent  #\aiCL\src\aiCL\
    CONFIG_PATH   = Path(__file__).resolve().parent / Path('./config')  #\aiCL\src\aiCL\config
    IMAGES_PATH = Path(__file__).resolve().parent.parent / Path("./resources/images") #A:\aiCL\src\aiCL\resources\entry_1.png   #resolve get the absolute.
    DATA_PATH   = Path(__file__).resolve().parent.parent / Path("./data")             #A:\aiCL\src\aiCL\data

    @staticmethod
    def img_file(path: str) -> Path:
        return Path_.IMAGES_PATH / Path(path)

    @staticmethod
    def data_file(path: str) -> Path:
        return Path_.DATA_PATH / Path(path)

    @staticmethod
    def config_file(path: str) -> Path:
        return Path_.ROOT_PATH / Path(path)


class User:
    load_dotenv()

    @staticmethod
    def username():
        username = os.getenv("LD_USR")
        return username
    
    @staticmethod
    def password():
        password = os.getenv("LD_KEY")
        return password


class WinPosition:
    @staticmethod
    def center(winobj, w, h):  # center
       
        # get screen width and height
        ws = winobj.winfo_screenwidth() # width of the screen
        hs = winobj.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        return w,h,x,y

    @staticmethod
    def rightbottom(winobj, w, h):  
       
        # get screen width and height
        ws = winobj.winfo_screenwidth() # width of the screen
        hs = winobj.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window

        x = ws - w - 20
        y = hs - h - 100

        return w,h,x,y

class Prompts:

    @staticmethod
    def assistant_instructions():
        assistant_instructions = (
            "The assistant will play the role of a job seeker. "
            "Based on the uploaded PDF resume and the job description, "
            "write a polite and professional job application message or cover letter to HR. "
            "Use professional language, integrate experiences and skills from the resume, "
            "and highlight strengths in relation to the job. "
            "Please start with the recruiter's name and end sincerely with resume's name "
            "This is a complete job application letter; exclude any content beyond it for easy automation.")

        return assistant_instructions
