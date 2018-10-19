### FIX
# when the home window (parameter and mode) is opened, the login window should close
# when change patient is select, the login window should reopen and the home window should close

### PARAMETERS
# not all parameters included are actually parameters to input a value - look into what each parameter means and fix accordingly
# set limits and/or create drop downs for parameters (some are enumerations or on/off)
# fill in more information page

### TIDY UP CODE
# implement a function that creates a label and entry box which returns the value

### MAYBE INCLUDE ???
# store the date and time

import tkinter
from tkinter import *

import csv

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

        # *** Register New User

        self.register = Label(master, text="Register New User")
        self.register.grid(row=1, column=2)

        # *** Username, Password, and Password Check

        self.unamelabel = Label(master, text="Username")
        self.unamelabel.grid(row=2, column=1, sticky=E)
        self.uname = Entry(master)
        self.uname.grid(row=2, column=2)

        self.pwordlabel = Label(master, text="Password")
        self.pwordlabel.grid(row=3,column=1, sticky=E)
        self.pword = Entry(master, show="*")
        self.pword.grid(row=3,column=2)
        
        self.pchecklabel = Label(master, text="Confirm Password")
        self.pchecklabel.grid(row=4,column=1, sticky=E)
        self.pcheck = Entry(master, show="*")
        self.pcheck.grid(row=4,column=2)

        self.register = Button(master, text="REGISTER", command = self.add_uname_pword)
        self.register.grid(row=5,column=2)

        # *** Login

        self.register = Label(master, text="Login")
        self.register.grid(row=1,column=4)

        # *** Username and Password

        self.unlabel = Label(master, text="Username")
        self.unlabel.grid(row=2,column=3, sticky=E)
        self.un = Entry(master)
        self.un.grid(row=2,column=4)

        self.pwlabel = Label(master, text="Password")
        self.pwlabel.grid(row=3,column=3, sticky=E)
        self.pw = Entry(master, show="*")
        self.pw.grid(row=3,column=4)

        self.register = Button(master, text="LOGIN", command = self.check_uname_pword)
        self.register.grid(row=5,column=4)

        # *** Return Users

        self.returnusers = Button(master, text="USERS", command = self.users)
        self.returnusers.grid(row=10,column=2)

        # *** Quit

        self.quit_button = Button(master, text="QUIT", command = master.destroy)
        self.quit_button.grid(row=10,column=3)

        # *** About

        self.about_button = Button(master, text="ABOUT", command = self.about)
        self.about_button.grid(row=10,column=4)

    # *** Method to register a username and password entered in the entry fields

    def add_uname_pword(self):
        if self.uname.get() in self.unames:
            User_Exists()
        else:
            if str(self.pword.get()) != str(self.pcheck.get()):
                Pass_No_Match()
            elif len(str(self.pword.get())) < 6:
                Pass_Too_Short()
            else:
                if len(self.unames) >= 10:
                    Too_Many_Users()
                else:
                    self.unames.append(self.uname.get())
                    self.pwords.append(self.pword.get())

                    sourceFile = open("data.csv", "a+")
                    sourceWriter = csv.DictWriter(sourceFile, fieldnames=['username', 'password'])
                    sourceWriter.writerow({'username' : self.uname.get(), 'password' : self.pword.get()})
                    sourceFile.close()

                    Successful_Registration()

    # *** Method to login a user using a username and password in the entry fields

    def check_uname_pword(self):
        if self.un.get() in self.unames:
            for i in range(len(self.unames)):
                if self.unames[i] == self.un.get() and self.pwords[i] == self.pw.get():
                    Successful_Login()
                elif self.unames[i] == self.un.get():
                    Wrong_Password()
        else:
            No_User()

    # *** Method to return a list of the currently registered usernames

    def users(self):
        win = Toplevel()
        win.wm_title("Registered Users")

        u = Label(win, text="Users:")
        u.grid(row=2, column=0)

        unames = Label(win, text=str(", ".join(self.unames)))
        unames.grid(row=2,column=1)

        b = Button(win, text="Okay", command=win.destroy)
        b.grid(row=4, column=0)

    # *** Method to return program and device information

    def about(self):
        win = Toplevel()
        win.wm_title("About Pacemaker Device Control Monitor v 1.0")

        u = Label(win, text="Pacemake Device Control Monitor 1.0 \n \n McMaster University: Department of Computing and Software \n Software Design 3K04 Fall 2018 \n \n Ventricle Capitalists (Group 7) \n \n Aurora Byrdon, Arthur Faron, Yansong (Kevin) Hu, \n David Lui, Michelle Monte, Erin Puersten, Daniel Su")
        u.grid(row=2, column=0)

        b = Button(win, text="Okay", command=win.destroy)
        b.grid(row=4, column=0)

##### POPUP and POPUP WINDOW DEFINITIONS

def Popup(popup_title,popup_description):
    win = Toplevel()
    win.wm_title(popup_title)

    l = Label(win, text=popup_description)
    l.grid(row=2, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=3, column=0)

def No_User():
    Popup("User not found","User not found, please try again")

def Wrong_Password():
    Popup("Password incorrect","Password incorrect, please try again")

def Successful_Registration():
    Popup("Registration Successful","Successfully registered")

def Too_Many_Users():
    Popup("Error","There are already 10 users registered for this program")

def Pass_No_Match():
    Popup("Error","The passwords you entered do not match")

def Pass_Too_Short():
    Popup("Error","Your password must be at least 6 characters long")

def User_Exists():
    Popup("Error","An account already exists under this username")
    
###### HOME PAGE WINDOW

class Home_Window(Frame):
    def __init__(self,master):

        self.pulse_width = 0
        self.pace_rate = 0
        self.pulse_amp = 0
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Home")

        self.title = Label(master, text="Welcome Back!")
        self.title.grid(row=1, column=3)

        # Selecting a Mode
        
        self.modelabel = Label(master, text="Select a Mode")
        self.modelabel.grid(row = 2, column = 4, pady=3, sticky=E)
        
        modes = [ 'OFF','VOO','AOO','VVT','AAT','VVI','AAI','VDD','DOO','DDI','DDD','AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR']
        mode = StringVar(master)
        mode.set(modes[0]) # set the default option
 
        modeMenu = OptionMenu(master, mode, *modes, command = self.change_mode)
        modeMenu.grid(row = 2, column = 5, pady=3, sticky=W)

        # Parameters

        self.prlabel = Label(master, text="Pace Rate")
        self.prlabel.grid(row=3, column=2, sticky=E, pady=3)
        self.pr = Entry(master, state='disabled')
        self.pr.grid(row=3,column=3, pady=3)
        
        #
        self.favdlabel = Label(master, text="Fixed AV Delay")
        self.favdlabel.grid(row=5, column=2, sticky=E)
        self.favd = Entry(master, state='disabled')
        self.favd.grid(row=5,column=3)

        self.davdlabel = Label(master, text="Dynamic AV Delay")
        self.davdlabel.grid(row=6, column=2, sticky=E)
        self.davd = Entry(master, state='disabled')
        self.davd.grid(row=6,column=3) #### ON OR OFF

        self.savdolabel = Label(master, text="Sensed AV Delay Offset")
        self.savdolabel.grid(row=7, column=2, sticky=E)
        self.savdo = Entry(master, state='disabled')
        self.savdo.grid(row=7,column=3)

        #
        self.msrlabel = Label(master, text="Maximum Sensor Rate")
        self.msrlabel.grid(row=9, column=2, sticky=E)
        self.msr = Entry(master, state='disabled')
        self.msr.grid(row=9,column=3)
        
        self.atlabel = Label(master, text="Activity Threshold")
        self.atlabel.grid(row=10, column=2, sticky=E)
        self.at = Entry(master, state='disabled')
        self.at.grid(row=10,column=3) ### ENumeration

        self.retlabel = Label(master, text="Reaction Time")
        self.retlabel.grid(row=11, column=2, sticky=E)
        self.ret = Entry(master, state='disabled')
        self.ret.grid(row=11,column=3)

        self.rflabel = Label(master, text="Response Factor")
        self.rflabel.grid(row=12, column=2, sticky=E)
        self.rf = Entry(master, state='disabled')
        self.rf.grid(row=12,column=3)

        self.rtlabel = Label(master, text="Recovery Time")
        self.rtlabel.grid(row=13, column=2, sticky=E)
        self.rt = Entry(master, state='disabled')
        self.rt.grid(row=13,column=3)

        #
        self.valabel = Label(master, text="Ventricular Amplitude")
        self.valabel.grid(row=3, column=4, sticky=E, pady=3)
        self.va = Entry(master, state='disabled')
        self.va.grid(row=3,column=5, pady = 3)

        self.vpwlabel = Label(master, text="Ventricular Pulse Width")
        self.vpwlabel.grid(row=4, column=4, sticky=E)
        self.vpw = Entry(master, state='disabled')
        self.vpw.grid(row=4,column=5)

        self.vslabel = Label(master, text="Ventricular Sensitivity")
        self.vslabel.grid(row=5, column=4, sticky=E)
        self.vs = Entry(master, state='disabled')
        self.vs.grid(row=5,column=5)

        #
        self.vrplabel = Label(master, text="VRP")
        self.vrplabel.grid(row=7, column=4, sticky=E)
        self.vrp = Entry(master, state='disabled')
        self.vrp.grid(row=7,column=5)
        
        self.arplabel = Label(master, text="ARP")
        self.arplabel.grid(row=8, column=4, sticky=E)
        self.arp = Entry(master, state='disabled')
        self.arp.grid(row=8,column=5)

        self.pvarplabel = Label(master, text="PVARP")
        self.pvarplabel.grid(row=9, column=4, sticky=E)
        self.pvarp = Entry(master, state='disabled')
        self.pvarp.grid(row=9,column=5)

        self.pvarpelabel = Label(master, text="PVARP Extension")
        self.pvarpelabel.grid(row=10, column=4, sticky=E)
        self.pvarpe = Entry(master, state='disabled')
        self.pvarpe.grid(row=10,column=5)

        #
        self.apwlabel = Label(master, text="Atrial Pulse Width")
        self.apwlabel.grid(row=3, column=6, sticky=E, pady=3)
        self.apw = Entry(master, state='disabled')
        self.apw.grid(row=3,column=7, pady=3)

        self.aalabel = Label(master, text="Atrial Amplitude")
        self.aalabel.grid(row=4, column=6, sticky=E)
        self.aa = Entry(master, state='disabled')
        self.aa.grid(row=4,column=7)

        self.aselabel = Label(master, text="Atrial Sensitivity")
        self.aselabel.grid(row=5, column=6, sticky=E)
        self.ase = Entry(master, state='disabled')
        self.ase.grid(row=5,column=7)

        #
        self.rslabel = Label(master, text="Rate Smoothing")
        self.rslabel.grid(row=7, column=6, sticky=E)
        self.rs = Entry(master, state='disabled')
        self.rs.grid(row=7,column=7)

        self.hlabel = Label(master, text="Hysteresis")
        self.hlabel.grid(row=8, column=6, sticky=E)
        self.h = Entry(master, state='disabled')
        self.h.grid(row=8,column=7)

        self.atrdlabel = Label(master, text="ATR Duration")
        self.atrdlabel.grid(row=10, column=6, sticky=E)
        self.atrd = Entry(master, state='disabled')
        self.atrd.grid(row=10,column=7)

        self.atrfmlabel = Label(master, text="ATR Fallback Mode")
        self.atrfmlabel.grid(row=11, column=6, sticky=E)
        self.atrfm = Entry(master, state='disabled')
        self.atrfm.grid(row=11,column=7) # ON or OFF

        self.atrftlabel = Label(master, text="ATR Fallback Time")
        self.atrftlabel.grid(row=12, column=6, sticky=E)
        self.atrft = Entry(master, state='disabled')
        self.atrft.grid(row=12,column=7)

        

        new_patient = Button(master, text="Change Patients", command=master.destroy) ### At the moment this only destroys the window, we need it to also repen the login window
        new_patient.grid(row=12, column=5)

        more_info = Button(master, text="More Information", command=More_Info)
        more_info.grid(row=12, column=4)

    def change_mode(self,mode):
        # if the mode is off - do not allow user to set anything
        if mode == 'OFF':
            self.pr.config(state='disabled')
            self.msr.config(state='disabled')
            self.favd.config(state='disabled')
            self.davd.config(state='disabled')
            self.aa.config(state='disabled')
            self.va.config(state='disabled')
            self.apw.config(state='disabled')
            self.vpw.config(state='disabled')
            self.ase.config(state='disabled')
            self.vs.config(state='disabled')
            self.vrp.config(state='disabled')
            self.arp.config(state='disabled')
            self.pvarp.config(state='disabled')
            self.h.config(state='disabled')
            self.rs.config(state='disabled')
            self.atrd.config(state='disabled')
            self.atrfm.config(state='disabled')
            self.atrft.config(state='disabled')
            self.at.config(state='disabled')
            self.ret.config(state='disabled')
            self.rf.config(state='disabled')
            self.rt.config(state='disabled')
        # if the mode is not off - allow user to set pulse rate
        else:
            self.pr.config(state='normal')

        # if the mode has rate modulation - allow user to set maximum sensor rate, activity threshold, reaction time, response time, and recovery time,
        # otherwise do not    
        if mode in {'AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR'}:
            self.msr.config(state='normal')
            self.at.config(state='normal')
            self.ret.config(state='normal')
            self.rf.config(state='normal')
            self.rt.config(state='normal')
        else:
            self.msr.config(state='disabled')
            self.at.config(state='disabled')
            self.ret.config(state='disabled')
            self.rf.config(state='disabled')
            self.rt.config(state='disabled')

        # if the mode has dual sensing - all the user to set fixed av delay, otherwise do not
        if mode in {'VDD','DOO','DDI','DDD','VDDR','DOOR','DDIR','DDDR'}:
            self.favd.config(state='normal')
            
            # of the modes with dual sensing, if the mode has dual tracked sensing - allow user to set atr duration, atr fallback mode,
            # atr fallback time, pvarp extension, and dynamic av delay,otherwise do not
            if mode in {'VDD','DDD','VDDR','DDDR'}:
                self.atrd.config(state='normal')
                self.atrfm.config(state='normal')
                self.atrft.config(state='normal')
                self.davd.config(state='normal')
                self.pvarpe.config(state='normal')
            
                # of the modes with dual tracked sensing, if the mode is dual chamber - allow user to set sensed av delay offset, otherwise do not
                if mode in {'DDD','DDDR'}:
                    self.savdo.config(state='normal')
                else:
                    self.savdo.config(state='disabled')
                
            else:
                self.atrd.config(state='disabled')
                self.atrfm.config(state='disabled')
                self.atrft.config(state='disabled')
                self.davd.config(state='disabled')
                self.savdo.config(state='disabled')
                self.pvarpe.config(state='disabled')

        else:
            self.atrd.config(state='disabled')
            self.atrfm.config(state='disabled')
            self.atrft.config(state='disabled')
            self.davd.config(state='disabled')
            self.savdo.config(state='disabled')
            self.savdo.config(state='disabled')
            self.favd.config(state='disabled')
            self.pvarpe.config(state='disabled')
            
        # if mode involves atrial pacing - allow user to set atrial amplitude and atrial pace width, otherwise do not
        if mode in {'AAT','AOO','AAI','DOO','DDI','DDD','AOOR','AAIR','DOOR','DDIR','DDDR'}:
            self.aa.config(state='normal')
            self.apw.config(state='normal')

            # if mode involves sensing of the atrial chamber - allow the user to set atrial sensitivity, atrial refractory period, and post ventricular
            # atrial refractory period, otherwise do not
            if mode in {'AAT','AAI','DDI','DDD','AAIR','DDIR','DDDR'}:
                self.ase.config(state='normal')
                self.arp.config(state='normal')
                self.pvarp.config(state='normal')
            else:
                self.ase.config(state='disabled')
                self.arp.config(state='disabled')
                self.pvarp.config(state='disabled')
        else:
            self.aa.config(state='disabled')
            self.apw.config(state='disabled')
            self.ase.config(state='disabled')
            self.arp.config(state='disabled')
            self.pvarp.config(state='disabled')

        # if mode involves ventricular pacing - allow the user to set venricular amplitude and ventricular pace width, otherwise do not
        if mode in {'VVT','VOO','VVI','VDD','DOO','DDI','DDD','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR'}:
            self.va.config(state='normal')
            self.vpw.config(state='normal')

            #if mode involves ventricular sensing - allow the user to set ventricular sensitivity and ventricular refractory period, otherwise do not
            if mode in {'VVT','VVI','VDD','DDI','DDD','VVIR','VDDR','DDIR','DDDR'}:
                self.vs.config(state='normal')
                self.vrp.config(state='normal')
            else:
                self.vs.config(state='disabled')
                self.vrp.config(state='disabled')
        else:
            self.va.config(state='disabled')
            self.vpw.config(state='disabled')
            self.vs.config(state='disabled')
            self.vrp.config(state='disabled')

        # if mode falls into list below - allow the user to set rate smoothing, otherwise do not
        if mode in {'AAI','VVI','AAIR','VVIR','DDD','DDDR','VDD','VDDR'}:
            self.rs.config(state='normal')

            # if mode falls into list below - allow the user to set hysterisis, otherwise do not
            if mode in {'AAI','VVI','AAIR','VVIR','DDD','DDDR'}:
                self.h.config(state='normal')
            else:
                self.h.config(state='disabled')
        else:
            self.rs.config(state='disabled')
            self.h.config(state='disabled')

def More_Info():
    Popup("Mode and Parameter Information","This is the information")

def Successful_Login():

    root = Tk()
    home = Home_Window(root)
    root.mainloop()
    
root = Tk()
my_window = Login_Window(root)
root.mainloop()
