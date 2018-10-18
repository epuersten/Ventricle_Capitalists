# Print messages into window - not terminal
# Store the date and time
# display the about information
# new patient function should be available everywhere

import tkinter
from tkinter import *
import csv


class Login_Window(Frame):
    def __init__(self,master):






        ################### FILE IO ##################
        self.unames = []
        self.pwords = []

        #Open the CSV we store the user/pass combos in
        try:
            sourceFile = open("data.csv", "r")
            sourceData = csv.DictReader(sourceFile, fieldnames=['username', 'password'])
        
            #Append to array of unames and passwords
            for row in sourceData:
                print(row['username'], row['password'])
                self.unames.append(row['username'])
                self.pwords.append(row['password'])
            
        except: #If file does not exist, create it
            sourceFile = open("data.csv", "w")
        #Close the file so we can re-open it in write mode later
        sourceFile.close()
        ##############################################
        





        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0")

        # Register New User

        self.register = Label(master, text="Register New User")
        self.register.grid(row=1, column=2)

        # Username, Password, and Password Check

        self.unamelabel = Label(master, text="Username")
        self.unamelabel.grid(row=2, column=1, sticky=E)
        self.uname = Entry(master)
        self.uname.grid(row=2, column=2)

        self.pwordlabel = Label(master, text="Password")
        self.pwordlabel.grid(row=3,column=1, sticky=E)
        self.pword = Entry(master)
        self.pword.grid(row=3,column=2)
        
        self.pchecklabel = Label(master, text="Confirm Password")
        self.pchecklabel.grid(row=4,column=1, sticky=E)
        self.pcheck = Entry(master)
        self.pcheck.grid(row=4,column=2)

        self.register = Button(master, text="REGISTER", command = self.add_uname_pword)
        self.register.grid(row=5,column=2)

        # Login

        self.register = Label(master, text="Login")
        self.register.grid(row=1,column=4)

        # Username and Password

        self.unlabel = Label(master, text="Username")
        self.unlabel.grid(row=2,column=3, sticky=E)
        self.un = Entry(master)
        self.un.grid(row=2,column=4)

        self.pwlabel = Label(master, text="Password")
        self.pwlabel.grid(row=3,column=3, sticky=E)
        self.pw = Entry(master)
        self.pw.grid(row=3,column=4)

        self.register = Button(master, text="LOGIN", command = self.check_uname_pword)
        self.register.grid(row=5,column=4)

        # Return Users

        self.returnusers = Button(master, text="USERS", command = self.users)
        self.returnusers.grid(row=10,column=2)

        # Quit

        self.quit_button = Button(master, text="QUIT", command = master.destroy)
        self.quit_button.grid(row=10,column=3)

        # About

        self.about_button = Button(master, text="ABOUT", command = self.about)
        self.about_button.grid(row=10,column=4)

    def add_uname_pword(self):
        if str(self.pword.get()) != str(self.pcheck.get()):
            print("Passwords do not match")
        else:
            if len(self.unames) >= 10:
                print("There are already 10 registered patients - you cannot add any more")
            else:
                print("You are now registering " + str(self.uname.get()) + " with password " + str(self.pword.get()) + " and password confirm " + str(self.pcheck.get()))
                self.unames.append(self.uname.get())
                self.pwords.append(self.pword.get())
                ############################## FILE IO ###########################################
                sourceFile = open("data.csv", "a+")
                sourceWriter = csv.DictWriter(sourceFile, fieldnames=['username', 'password'])
                sourceWriter.writerow({'username' : self.uname.get(), 'password' : self.pword.get()})
                sourceFile.close()
                ################################################################################

    def check_uname_pword(self):
        print(self.un.get())
        print(self.unames[0])
        if self.un.get() in self.unames:
            for i in range(len(self.unames)):
                if self.unames[i] == self.un.get() and self.pwords[i] == self.pw.get():
                    print("Welcome back " + self.un.get())
                    Successful_Login()
                elif self.unames[i] == self.un.get():
                    Wrong_Password()
        else:
            No_User()

    def users(self):
        print(self.unames)
        print(self.pwords)

    def about(self):
        print("hello")

    def date_time(self):
        print("hello")
        #popup window to input the date and time and store them in variables5

        

def No_User():
    win = Toplevel()
    win.wm_title("User not found")

    l = Label(win, text="User not found, please try again")
    l.grid(row=2, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=3, column=0)

def Wrong_Password():
    win = Toplevel()
    win.wm_title("Password incorrect")

    l = Label(win, text="Password is incorrect, please try again")
    l.grid(row=2, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=3, column=0)

def Successful_Login():
    win = Toplevel()
    win.wm_title("Home")

    l = Label(win, text="Successful Login")
    l.grid(row=2, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=3, column=0)



root = Tk()
my_window = Login_Window(root)
root.mainloop()
