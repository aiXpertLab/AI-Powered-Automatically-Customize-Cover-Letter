import tkinter as tk
import tkinter.messagebox as msgbox

from utils.utilities import CopyResume,KeyGood, ExceptionHandler
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
            result = msgbox.askyesno('Confirm', 
                "The app will open the browser and initiate a login attempt using the provided Username and Password."
                "\n\nIn the event of requiring verification or encountering mismatched credentials, users are advised to proceed with manual login through the opened browser."
                "\n\nKindly select 'Yes' to proceed or 'No' to return.") 
            # hw.attributes('-topmost', True)
            if result:
                hw.withdraw()
                hw.fun.login(user_name, pass_word)            # login linkedin for a long time
                hw.deiconify()
                hw.ui.def_small_canvas(hw)
                hw.ui.def_textbox(hw)
                hw.ui.def_textbox_content(hw, "Step 1. Locate your preferred job in the opened browser window.\n\n"
                        "Step 2. Once found, click on the title of the desired job in the browser window."
                        "\n\nStep 3. Select the <<<Scrape>>> button on the left-hand side to display the job description here.")
            else:
                pass
                
        elif clicked == 'scrape':
            try:hw.can_key.destroy()
            except:pass
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
           
            hw.client = KeyGood.check_key()     #check windows key
            if hw.client is None:
                key = hw.ui.def_key_screen(hw)        # key is in hw.openai_key
                # hw.openai_key = hw.entry_key.get()
            else:
                hw.ui.def_text_bottom(hw,"<<< AI is generating the cover letter ....")
                hw.scrape_2_cl() 
        
        elif clicked == 'continue':
            hw.client = KeyGood.check_key(hw.entry_key.get())      # 2. check key 
            if hw.client is None:
                msgbox.showerror(title="Error Code 401 - OpenAI Invalid Authentication", message="Quick fix: \n1. Register and create a free key with OpenAI.\n2. Set up your key on your device.\n3. Try again!")
                key = hw.ui.def_key_screen(hw)        # key is in hw.openai_key
            else:
                hw.ui.def_text_bottom(hw,"<<< AI is generating the cover letter ....")
                hw.scrape_2_cl() 
# #---------------------------------------------------------------------------------------------------------
        elif clicked == 'help':
            try:hw.can_key.destroy()
            except:pass
            hw.can_small.delete(hw.head1)
            hw.can_small.delete(hw.head2)
            hw.head1 = hw.can_small.create_text(190,  20   ,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 15 * -1),text="AI-Powered Auto Cover Letter",)
            hw.head2 = hw.can_small.create_text(190, 20 +40,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 14 * -1),text="FAQ: ",)
            hw.ui.def_text_bottom(hw,"http://hypech.com for more information.")
            content='1. Currently supports Chrome browser. Download the official Chrome Driver from https://googlechromelabs.github.io/chrome-for-testing/.\n'\
                    '2. Follow the instructions on http://openai.com to obtain and use your API key.\n'\
                    '3. Update your resume by clicking here.\n'\
                    '4. Double-check your cover letter before sending it out.\n'\
                    '5. Contact us via email: aiXpertLab@gmail.com for any questions.\n\n'\
                    'Start using this powerful tool to improve your job search today!'
            hw.ui.def_textbox(hw, "scroll")
            hw.ui.def_textbox_content(hw, content) 

        elif clicked == 'logout':
            hw.destroy()

        else: # rest
            print(32)


    def scrape_2_cl(hw):
        cl_obj = AI(hw.job_desc, hw.client)
        cover_letter=cl_obj.ai()
        try:hw.can_key.destroy()
        except:pass
        hw.can_small.itemconfig(hw.head1, text = hw.job_title_40)
        hw.can_small.itemconfig(hw.head2, text = hw.job_company_first2part)
        hw.ui.def_textbox(hw, "scroll")
        hw.ui.def_textbox_content(hw, cover_letter)
        hw.ui.def_text_bottom(hw," Cover Letter is ready. Copy/paste it.")
