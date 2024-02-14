import tkinter as tk
import webbrowser

from tkinter    import Canvas, PhotoImage, Entry, Button, Frame, Text, scrolledtext, END
from functools  import partial

from config.config   import WinPosition, Path_, User
from utils.utilities import HyperlinkManager, ChangeText, ExceptionHandler

class UIDef:

    def def_hw_window(self, hw):
        hw.title("AI-Powered Auto Customize and Send Cover Letter")
        hw.geometry('%dx%d+%d+%d' % WinPosition.center(hw,1000,500))
        hw.attributes('-topmost', True)
        hw.attributes('-alpha', 1)
        hw.iconphoto(False, tk.PhotoImage(file=Path_.img_file("icon.png")))
        hw.resizable(False, False)

    def def_login_canvas(self, hw):
        hw.canv_login = Canvas(hw, bg="#5E95FF", height=500, width=1000, bd=0, highlightthickness=0, relief="ridge")
        hw.canv_login.place(x=0, y=0)
        hw.canv_login.create_rectangle(480, 0, 1000, 500, fill="white", outline="")

    def def_login_canvas_elements(self, hw):
        hw.entry_image_1 = PhotoImage(file=Path_.img_file("entry_1.png"))
        image_id1 = hw.canv_login.create_image(736, 331, image=hw.entry_image_1)
        entry_1 = Entry(hw, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_1.place(x=568, y=294, width=336, height=0)

        hw.entry_image_2 = PhotoImage(file=Path_.img_file("entry_2.png"))
        bk2 = hw.canv_login.create_image(736, 229, image=hw.entry_image_2)
        entry_2 = Entry(hw, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_2.place(x=568, y=192, width=336, height=0)

        hw.image_alice = PhotoImage(file=Path_.img_file("alice.png"))
        hw.canv_login.create_image(420, 340, image=hw.image_alice)

        i, j, k = 20, 240, 55

        hw.canv_login.create_text( 40, i ,   anchor="nw",fill="white",font=("Montserrat Bold", 50 * -1),text="AI-Powered ",)
        hw.canv_login.create_text( 40, i+65, anchor="nw",fill="white",font=("Montserrat Bold", 50 * -1),text="Auto-Customize",)
        hw.canv_login.create_text( 45, i+130,anchor="nw",fill="white",font=("Montserrat Bold", 50 * -1),text="Cover Letter",)
        hw.canv_login.create_text( k, j ,    anchor="nw",fill="white",font=("Montserrat", 18 * -1),text="Automatically scrape job details",)
        hw.canv_login.create_text( k, j + 40,anchor="nw",fill="white",font=("Montserrat", 18 * -1),text="Seamlessly combine resume and ",)
        hw.canv_login.create_text( k, j + 80,anchor="nw",fill="white",font=("Montserrat", 18 * -1),text="job description",)
        hw.canv_login.create_text( k, j +120,anchor="nw",fill="white",font=("Montserrat", 18 * -1),text="Automatically customize cover letter",)
        hw.canv_login.create_text( k, j +160,anchor="nw",fill="white",font=("Montserrat", 18 * -1),text="Your dream job awaits!",)
        
        hw.canv_login.create_text( 90,    460,anchor="nw",fill="white",font=("Montserrat Bold", 18 * -1),text="© aiXpertLab, 2024",)

        hw.canv_login.create_text(553,130,anchor="nw",fill="#CCCCCC",font=("Montserrat Bold", 16 * -1),text="Enter the email/password for Linkedin.",)
        hw.canv_login.create_text(573,306,anchor="nw",fill="#5E95FF",font=("Montserrat Bold", 14 * -1),text="Linkedin Password",)
        hw.canv_login.create_text(573,204,anchor="nw",fill="#5E95FF",font=("Montserrat Bold", 14 * -1),text="Linkedin Email",)
        hw.canv_login.create_text(553,66, anchor="nw",fill="#5E95FF",font=("Montserrat Bold", 26 * -1),text="Login to Linkedin to start",)
        
        hw.entry_obj_usr = Entry(hw.canv_login,bd=0,bg="#EFEFEF",highlightthickness=0,font=("Montserrat Bold", 16 * -1),foreground="#777777",)
        hw.entry_obj_usr.insert(0, User.username())  # Insert default value
        hw.entry_obj_usr.place(x=573, y=229, width=326, height=22)

        hw.entry_obj_pwd = Entry(hw.canv_login,bd=0,bg="#EFEFEF",highlightthickness=0,font=("Montserrat Bold", 16 * -1),foreground="#777777",show="•",)
        hw.entry_obj_pwd.insert(0, User.password())  # Insert default value
        hw.entry_obj_pwd.place(x=573, y=330, width=326, height=22)

        hw.login_image = PhotoImage(file=Path_.img_file("login.png"))
        hw.btn_login = Button(hw.canv_login,image=hw.login_image,borderwidth=0,highlightthickness=0,relief="flat", command=lambda: hw.button_click(hw.btn_login, "login"),)
        hw.btn_login.place(x=641, y=412, width=190, height=48)

        hw.entry_obj_usr.bind("<Return>", lambda x: hw.button_click(hw.btn_login, "login"))
        hw.entry_obj_pwd.bind("<Return>", lambda x: hw.button_click(hw.btn_login, "login"))
        hw.bind("<Return>", lambda event: hw.button_click(hw.btn_login, "login"))

    def def_small_canvas(self, hw):
        
        hw.geometry('%dx%d+%d+%d' % WinPosition.rightbottom(hw,560,350))
        hw.attributes('-alpha', 0.95)
        hw.canv_login.destroy()

        hw.can_small = Canvas(hw, bg="#5E95FF", width=560,height=350,  bd=0, highlightthickness=0, relief="ridge")
        hw.can_small.place(x=0, y=0)
        hw.can_small.create_rectangle(180, 0, 560, 350, fill="white", outline="")       # start (180,0) total width 560, height 350, white width 380

        hw.sidebar_indicator = Frame(hw, background="white", height=47, width=7)  

        hw.scrape_img      = PhotoImage(file=Path_.img_file("scrape.png"))
        hw.coverletter_img = PhotoImage(file=Path_.img_file("coverletter.png"))
        hw.help_img        = PhotoImage(file=Path_.img_file("help.png"))
        hw.logout_img      = PhotoImage(file=Path_.img_file("logout.png"))

        hw.btn_scrape     = Button(hw.can_small,image=hw.scrape_img,     cursor='hand2', activebackground="#5E95FF",borderwidth=0,highlightthickness=0,relief="flat",command=lambda: hw.button_click(hw.btn_scrape, "scrape"),)
        hw.btn_coverletter= Button(hw.can_small,image=hw.coverletter_img,cursor='hand2', activebackground="#5E95FF",relief="flat",borderwidth=0,highlightthickness=0,command=lambda: hw.button_click(hw.btn_coverletter, "coverletter"),)
        hw.btn_help       = Button(hw.can_small,image=hw.help_img,       cursor='hand2', activebackground="#5E95FF",relief="flat",borderwidth=0,highlightthickness=0,command=lambda: hw.button_click(hw.btn_help,  "help"),)
        hw.btn_logout     = Button(hw.can_small,image=hw.logout_img,     cursor='hand2', relief="flat",borderwidth=0,highlightthickness=0,           command=lambda: hw.button_click(hw.btn_logout,"logout"),)

        hw.btn_scrape.place(x=7, y=83, width=173, height=47)
        hw.btn_coverletter.place(x=7, y=133, width=173, height=47)
        hw.btn_help.place(x=7, y=183, width=173, height=47)
        hw.btn_logout.place(x=0, y=283, width=173, height=47)

        hw.title    = hw.can_small.create_text(20,  15,anchor="nw",fill="white",font=("Montserrat Bold", 48 * -1),               text="ai CL",)
        hw.line_img = PhotoImage(file=Path_.img_file("line.png"))
        hw.line     = hw.can_small.create_image(190, 20 +32, anchor="nw", image=hw.line_img)  #35
        hw.head1    = hw.can_small.create_text(190,  20   ,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 15 * -1),text="AI-Powered Auto Cover Letter",)
        hw.head2    = hw.can_small.create_text(190,  20 +40,anchor="nw",fill="#5E95FF",font=("Montserrat SemiBold", 14 * -1),text="Easy Steps: ",)

        hw.square_img = PhotoImage(file=Path_.img_file("white_square_1.png"))
        hw.square     = hw.can_small.create_image(190, 20+68, anchor="nw", image=hw.square_img)

        hw.bind("<Return>", lambda event: hw.button_click(hw.btn_coverletter, "coverletter"),)
        hw.bind("<F1>"    , lambda event: hw.button_click(hw.btn_logout, "logout"))

    def def_textbox(self,hw, scroll="none"):
        try:hw.can_key.destroy()
        except Exception as e: pass

        if scroll == 'scroll':
            hw.txt_box= scrolledtext.ScrolledText(hw.can_small, wrap="word",bd=0,bg="#EFEFEF",relief='groove', highlightthickness=0,font=("Montserrat", 14 * -1),foreground="#777777")
        else:
            hw.txt_box = Text(hw.can_small, wrap="word",bd=0,bg="#EFEFEF", relief='groove', highlightthickness=0,font=("Montserrat", 14 * -1),foreground="#393D47")
        
        hw.txt_box.place(x=190 + 7, y=20 +75, width=322, height=210)

    def def_textbox_content(self, hw, content="Intentionally blank."):
        self.content = content
        print(self.content)
        
        try:
            hw.txt_box.delete("1.0", tk.END)
        except Exception as e: ExceptionHandler.handle_exception(e,"try:hw.txt_box.delete")

        hw.txt_box.insert("2.0", self.content)

        if True:
            ChangeText.bold_text(hw.txt_box, "browser just opened")
        else:
            ChangeText.bold_text(hw.txt_box, "kkk")


    def def_text_bottom(self, hw,text):
        try:hw.can_small.delete(hw.bottom)
        except:pass

        hw.bottom   = hw.can_small.create_text(190, 320,anchor="nw",fill="#5E95FF",font=("Montserrat", 12 * -1),text=text)

    def def_key_screen(self, hw):
        try:hw.can_key.destroy()
        except:pass
        hw.can_small.itemconfig(hw.head2, text="")
        hw.can_small.itemconfig(hw.head1, text="")                                                                            
        hw.head1 = hw.can_small.create_text(190, 20, anchor="nw", fill="#5E95FF", font=("Montserrat SemiBold", 14 * -1), text="Start with OpenAI API for ChatGPT",)
        hw.head2 = hw.can_small.create_text(190, 60, anchor="nw", fill="#5E95FF", font=("Montserrat SemiBold", 14 * -1), text="Get Free Access in Easy Steps:",)

        hw.can_key = Canvas(hw, bg="white", height=560, width=350, bd=0, highlightthickness=0, relief="ridge")
        hw.can_key.place(x=190, y=85)

        hw.key_txt = Text(hw.can_key, wrap="word",bd=0, height=40,width=20,relief='groove', highlightthickness=0,font=("Montserrat", 14 * -1),foreground="#777777")
        hw.key_txt.place(x=0, y=5, width=330, height=100)

        hyperlink= HyperlinkManager(hw.key_txt)
        hw.key_txt.insert("1.0","Step 1: ")
        hw.key_txt.insert(END, "Register ", hyperlink.add(partial(webbrowser.open,"https://platform.openai.com/api-keys")))
        hw.key_txt.insert(END, " and ")
        hw.key_txt.insert(END, "Create a Free Key", hyperlink.add(partial(webbrowser.open,"https://platform.openai.com/api-keys")))
        hw.key_txt.insert(END, " with OpenAI.\n\n")
        hw.key_txt.insert(END, "Step 2: ")
        hw.key_txt.insert(END, "Configure Your API Key", hyperlink.add(partial(webbrowser.open,"https://platform.openai.com/docs/quickstart?context=python")))
        hw.key_txt.insert(END, " on Your Device or Input the Key Provided Below.",)

        hw.entry_key_img = PhotoImage(file=Path_.img_file("entry_key.png"))
        hw.can_key.create_image(0, 115, anchor="nw", image=hw.entry_key_img)
        hw.entry_key_bg = Entry(hw.can_small, bd=0, bg="#EFEFEF", highlightthickness=0)
        hw.can_key.create_text(10, 125, anchor="nw",fill="#5E95FF",font=("Montserrat Bold", 14 * -1),text="OpenAI API Key:",)

        hw.entry_key = Entry(hw.can_key, bd=0, bg="#EFEFEF",highlightthickness=0,font=("Montserrat", 12 * -1),foreground="#777777",)
        hw.entry_key.insert(0, 'sk-ReplaceThisWithYourKey')  # Insert default value
        hw.entry_key.place(x=10 , y= 145, width=300, height=24)

        hw.continue_img = PhotoImage(file=Path_.img_file("continue.png"))
        hw.btn_continue = Button(hw.can_key,image=hw.continue_img,borderwidth=0,highlightthickness=0,relief="flat", command=lambda: hw.button_click(hw.btn_coverletter, "continue"),)
        hw.btn_continue.place(x=120 , y=20 + 185 )

        hw.bind("<Return>", lambda event: hw.button_click(hw.btn_continue, "continue"))
        return()

    def destroy(self, hw):
        try: hw.txt_box.place_forget() 
        except: pass

        try:hw.can_small.delete(hw.bottom)
        except:pass

        try:hw.can_key.destroy()
        except:pass

