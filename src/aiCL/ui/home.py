import tkinter as tk
import tkinter.messagebox as msgbox

from tkinter    import PhotoImage, Entry, Button, Text, END, messagebox
from functools  import partial

from config.config   import Path_
from utils.utilities import CopyResume, CheckKeyInComputer, ObjPrinter, ExceptionHandler
from ui.ui_def       import UIDef
from functions.login_scrape     import LoginScrape
from functions.ai import AI


class Home(tk.Tk):
    def __init__(hw):
        super().__init__()

        hw.fun= LoginScrape()
        hw.ui = UIDef()
        hw.ui.def_hw_window(hw)
        hw.ui.def_login_canvas(hw)
        hw.ui.def_login_canvas_elements(hw)


#---------------------------------------------------------------------------------------------------------
    def button_click(hw, caller, clicked):
        if clicked != 'login':
            hw.sidebar_indicator.place(x=0, y=caller.winfo_y())

        if clicked == "login":
            user_name = hw.entry_obj_usr.get().lower()
            pass_word = hw.entry_obj_pwd.get()
            result = msgbox.askyesno('Confirm', "The app will open the browser and try to login with the Username and Password provided. \n\nIf need verification, or username/password not match, please continue login in the browser opened manually. \n\nPlease press Yes to continue, or No to go back. ") 
            # hw.attributes('-topmost', True)
            if result:
                hw.withdraw()
                hw.fun.login(user_name, pass_word)            # login linkedin for a long time
                hw.deiconify()
                hw.ui.def_small_canvas(hw)
                hw.ui.def_textbox(hw)
                hw.ui.def_textbox_content(hw, "Step 1. Find your favorite job in the browser just opened.\n\n"
                        "Step 2. Click the job title in the browser just opened."
                        "\n\nStep 3. Click <<<Scrape>>> button on left, to show job description here.")
            else:
                pass
                
        elif clicked == 'scrape':
            job_title, job_company, hw.job_desc = hw.fun.scrape_title_corp_desc()
            hw.job_title_40 = job_title.split(',')[0].strip()[:42]
            parts_job_company = job_company.split('·')
            hw.job_company_first2part = '·'.join(parts_job_company[:2]).strip()[:44]

            hw.can_small.itemconfig(hw.head1, text = hw.job_title_40)
            hw.can_small.itemconfig(hw.head2, text = hw.job_company_first2part)
            hw.ui.def_text_bottom(hw,"<<< click Cover Letter to continue.")

            hw.ui.def_textbox(hw, "scroll")
            hw.ui.def_textbox_content(hw, hw.job_desc)

        elif clicked == 'coverletter':
            result = CopyResume.copy_and_rename_file()                         # 1. check resume
            if result == "existed":
                hw.ui.def_text_bottom(hw," Resume is ready.")
            elif result == 'succeed':
                hw.ui.def_text_bottom(hw," Resume has been successfuly updated.")
            
            key_env = CheckKeyInComputer.check_key_in_computer()      # 2. check key 
            if not key_env:
                key = hw.ui.def_key_screen(hw)        # key is in hw.openai_key
            # hw.ui.def_text_bottom(hw,"<<< click Scrape for a new opportunity.")
        
        elif clicked == 'continue':
            
            key_env = CheckKeyInComputer.check_key_in_computer()      # 2. check key 
            hw.openai_key = hw.entry_key.get()
            hw.ui.def_text_bottom(hw,"<<< AI is generating the cover letter ....")
            hw.scrape_2_cl() 

# #---------------------------------------------------------------------------------------------------------
        elif clicked == 'help':
            hw.can_small.delete(hw.head1)
            hw.can_small.delete(hw.head2)
            hw.head1 = hw.can_small.create_text(190,  20   ,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 15 * -1),text="AI-Powered Auto Cover Letter",)
            hw.head2 = hw.can_small.create_text(190, 20 +40,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 14 * -1),text="FAQ: ",)
            hw.ui.def_text_bottom(hw,"http://hypech.com for more information.")

            content='1. Please visit http://hypech.com/ai for detailed information.\n\n'\
                    '2. Only support Chrome for now. Others will be followed.\n\n'\
                    '3. Download official Chrome Driver from https://googlechromelabs.github.io/chrome-for-testing/.\n\n'\
                    '4. To update your resume, click here:\n\n'\
                    '5. Follow http://openai.com to get your key, and setup your key in computer environment.\n\n'\
                    '6. Test your key here to confirm you setup your key in your computer correctly.'\
                    '7. Before sending out the cover letter, please double triple check to make sure it relfects your own idea.\n\n'\
                    '8. We can be reached: Linkedin: X(Twiter): Facebook: Github. Email: '
            hw.ui.def_textbox(hw, "scroll")
            hw.ui.def_textbox_content(hw, content) 

        elif clicked == 'logout':
            hw.destroy()

        else: # rest
            print(32)


    def scrape_2_cl(hw):
        cl_obj = AI(hw.job_desc, hw.openai_key)
        cover_letter=cl_obj.ai()

        hw.can_key.destroy()
        hw.can_small.itemconfig(hw.head1, text = hw.job_title_40)
        hw.can_small.itemconfig(hw.head2, text = hw.job_company_first2part)
        hw.ui.def_textbox(hw, "scroll")
        hw.ui.def_textbox_content(hw, cover_letter)
        hw.ui.def_text_bottom(hw," Cover Letter is ready. Copy/paste it.")
