
import csv
import tkinter
from tkinter import *
from _HomeWindow import *

#************************ LOGIN WINDOW ***************************

class Login_Window(Frame):
    def __init__(self,master):

        self.unames = []
        self.pwords = []

        #************************ RETRIEVE LOGIN/PASSWORD INFORMATION ***************************

        try: #Open the CSV we store the user/pass combos in
            sourceFile = open("data.csv", "r")
            sourceData = csv.DictReader(sourceFile, fieldnames=['username', 'password'])
        
            #Append to array of unames and passwords
            for row in sourceData:
                self.unames.append(row['username'])
                self.pwords.append(row['password'])
            
        except: #If file does not exist, create it
            sourceFile = open("data.csv", "w")
        #Close the file so we can re-open it in write mode later
        sourceFile.close()
        #****************************************************************************************
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 2.0")
        master.config(background='white')

        Label(master, text='Pacemaker Device Control Monitor', bg = 'white', font = 12).grid(row=1,column=1)

        f1 = Frame(master, bg = 'gray92', padx = 20)
        f1.grid(row = 2, column = 1, padx = 20)

        reg_frame = Frame(f1, bg = 'gray92', padx = 10, pady = 10)
        reg_frame.grid(row=1, column=1)

        login_frame = Frame(f1, bg = 'gray92', padx = 10, pady = 10)
        login_frame.grid(row=1, column=2)

        button_frame = Frame(master, bg = 'white', padx = 10, pady = 10)
        button_frame.grid(row=3, column=1)
        
        # *** Create Register Entry Fields (Labels, Entry, and Button)

        Label(reg_frame, text="Register", font=5, bg = 'gray92').grid(row=1, column=2)

        Label(reg_frame, text="Username", bg = 'gray92').grid(row=2, column=1, sticky=E)
        self.uname = Entry(reg_frame, bg = 'white smoke')
        self.uname.grid(row=2, column=2)

        Label(reg_frame, text="Password", bg = 'gray92').grid(row=3,column=1, sticky=E)
        self.pword = Entry(reg_frame, show="*", bg = 'white smoke')
        self.pword.grid(row=3,column=2)
        
        Label(reg_frame, text="Confirm Password", bg = 'gray92').grid(row=4,column=1, sticky=E)
        self.pcheck = Entry(reg_frame, show="*", bg = 'white smoke')
        self.pcheck.grid(row=4,column=2)

        Button(reg_frame, text="Register", command = self.__add_uname_pword, bg='royal blue', fg = 'white').grid(row=5,column=2)

        # *** Create Login Entry Fields (Labels, Entry, and Button)

        Label(login_frame, text="Login", font=5, bg = 'gray92').grid(row=1,column=2)

        Label(login_frame, text="Username", bg = 'gray92').grid(row=2,column=1, sticky=E)
        self.un = Entry(login_frame, bg = 'white smoke')
        self.un.grid(row=2,column=2)

        Label(login_frame, text="Password", bg = 'gray92').grid(row=3,column=1, sticky=E)
        self.pw = Entry(login_frame, show="*", bg = 'white smoke')
        self.pw.grid(row=3,column=2)

        Button(login_frame, text="Login", command = self.__check_uname_pword, bg = 'royal blue', fg = 'white').grid(row=4,column=2)

        # *** Create Buttons (Users, Quit, and About)

        Button(button_frame, text="Users", command = self.__users, bg = 'royal blue', fg = 'white', padx = 10).grid(row=1,column=1, padx = 10, pady = 10)
        Button(button_frame, text="About", command = self.__about, bg = 'royal blue', fg = 'white', padx = 10).grid(row=1,column=2, padx = 10, pady = 10)
        Button(button_frame, text="QUIT", command = master.destroy, bg = 'red', fg = 'white').grid(row=1,column=3, padx = 10, pady = 10)

    # *** Method to register a username and password entered in the entry fields

    def __add_uname_pword(self):
        if self.uname.get() in self.unames:
            self.__user_exists()
        else:
            if str(self.pword.get()) != str(self.pcheck.get()):
                self.__pass_no_match()
            elif len(str(self.pword.get())) < 6:
                self.__pass_too_short()
            else:
                if len(self.unames) >= 10:
                    self.__too_many_users()
                else:
                    self.unames.append(self.uname.get())
                    self.pwords.append(self.pword.get())

                    sourceFile = open("data.csv", "a+")
                    sourceWriter = csv.DictWriter(sourceFile, fieldnames=['username', 'password'])
                    sourceWriter.writerow({'username' : self.uname.get(), 'password' : self.pword.get()})
                    sourceFile.close()

                    self.__successful_registration()

    # *** Method to login a user using a username and password in the entry fields

    def __check_uname_pword(self):
        if self.un.get() in self.unames:
            for i in range(len(self.unames)):
                if self.unames[i] == self.un.get() and self.pwords[i] == self.pw.get():
                    self.__successful_login()
                elif self.unames[i] == self.un.get():
                    self.__wrong_password()
        else:
            self.__no_user()

    # *** Method to return a list of the currently registered usernames

    def __users(self):
        win = Toplevel()
        win.wm_title("Registered Users")
        win.config(bg = 'white')

        Label(win, text="Users:", bg = 'white').grid(row=2, column=0)
        Label(win, bg = 'white', text=str(", ".join(self.unames))).grid(row=2,column=1)
        Button(win, text="Okay", command=win.destroy).grid(row=4, column=1)

    # *** Method to return program and device information

    def __about(self):
        win = Toplevel()
        win.wm_title("About Pacemaker Device Control Monitor v 2.0")
        win.config(bg = 'white')

        Label(win,bg='white', text = 'Pacemake Device Control Monitor 2.0').grid(row=1, column =1)

        Label(win, bg = 'white', justify = LEFT, text="""
        McMaster University: Department of Computing and Software
        Software Design 3K04 Fall 2018

        Ventricle Capitalists (Group 7)
        Aurora Brydon, Arthur Faron, Yansong (Kevin) Hu,
        David Lui, Michelle Monte, Erin Puersten, Daniel Su""").grid(row=2, column=1)
        Button(win, text="Okay", command=win.destroy).grid(row=3, column=1)

    # *** Popup window methods
        
    def __no_user(self):
        Popup("Error","User not found, please try again")

    def __wrong_password(self):
        Popup("Error","Password incorrect, please try again")

    def __successful_registration(self):
        Popup("Registration Successful","Successfully registered")

    def __too_many_users(self):
        Popup("Error","There are already 10 users registered for this program")

    def __pass_no_match(self):
        Popup("Error","The passwords you entered do not match")

    def __pass_too_short(self):
        Popup("Error","Your password must be at least 6 characters long")

    def __user_exists(self):
        Popup("Error","An account already exists under this username")

    def __successful_login(self):
        self.homeWindow = Toplevel(self.master)
        self.loginWindow = Home_Window(self.homeWindow, self.un.get())
        #Home_Window.username = self.un.get()
