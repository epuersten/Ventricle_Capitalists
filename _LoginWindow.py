import csv
import tkinter
from tkinter import *
from _PopupWindow import *
from _PopupWindow import *
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
        master.title("Pacemaker Device Control Monitor v 1.0")

        # *** Create Register Entry Fields (Labels, Entry, and Button)

        Label(master, text="Register New User").grid(row=1, column=2)

        Label(master, text="Username").grid(row=2, column=1, sticky=E)
        self.uname = Entry(master)
        self.uname.grid(row=2, column=2)

        Label(master, text="Password").grid(row=3,column=1, sticky=E)
        self.pword = Entry(master, show="*")
        self.pword.grid(row=3,column=2)
        
        Label(master, text="Confirm Password").grid(row=4,column=1, sticky=E)
        self.pcheck = Entry(master, show="*")
        self.pcheck.grid(row=4,column=2)

        Button(master, text="REGISTER", command = self.__add_uname_pword).grid(row=5,column=2)

        # *** Create Login Entry Fields (Labels, Entry, and Button)

        Label(master, text="Login").grid(row=1,column=4)

        Label(master, text="Username").grid(row=2,column=3, sticky=E)
        self.un = Entry(master)
        self.un.grid(row=2,column=4)

        Label(master, text="Password").grid(row=3,column=3, sticky=E)
        self.pw = Entry(master, show="*")
        self.pw.grid(row=3,column=4)

        Button(master, text="LOGIN", command = self.__check_uname_pword).grid(row=5,column=4)

        # *** Create Buttons (Users, Quit, and About)

        Button(master, text="USERS", command = self.__users).grid(row=10,column=2)

        Button(master, text="QUIT", command = master.destroy).grid(row=10,column=3)

        Button(master, text="ABOUT", command = self.__about).grid(row=10,column=4)

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

        Label(win, text="Users:").grid(row=2, column=0)
        Label(win, text=str(", ".join(self.unames))).grid(row=2,column=1)
        Button(win, text="Okay", command=win.destroy).grid(row=4, column=0)

    # *** Method to return program and device information

    def __about(self):
        win = Toplevel()
        win.wm_title("About Pacemaker Device Control Monitor v 1.0")

        Label(win, text="""Pacemake Device Control Monitor 1.0

              McMaster University: Department of Computing and Software
              Software Design 3K04 Fall 2018
              Ventricle Capitalists (Group 7)

              Aurora Brydon, Arthur Faron, Yansong (Kevin) Hu, \n David Lui, Michelle Monte, Erin Puersten, Daniel Su""").grid(row=2, column=0)
        Button(win, text="Okay", command=win.destroy).grid(row=4, column=0)

    # *** Popup window methods
        
    def __no_user(self):
        Popup("User not found","User not found, please try again")

    def __wrong_password(self):
        Popup("Password incorrect","Password incorrect, please try again")

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
        self.loginWindow = Home_Window(self.homeWindow)