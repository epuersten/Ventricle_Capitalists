### TO DO
# tidy up the code
# press random key and bring up device detected window (asks would you like to interrogate the device)

### PARAMETERS
# figure out how to return from a checkbox
# some parameters are only available if a checkbox is ticked - grey them out if the checkbox is not ticked
# add minimum dynamic av delay and ventricular blanking???

### MAYBE INCLUDE ???
# store the date and time

import tkinter
from tkinter import *

import csv

##### POPUP WINDOW DEFINITION

def Popup(popup_title,popup_description):
    win = Toplevel()
    win.wm_title(popup_title)

    Label(win, text=popup_description).grid(row=2, column=0)
    Button(win, text="Okay", command=win.destroy).grid(row=3, column=0)

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

        # *** Register New User (Label, Entry Fields, and Button)

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

        Button(master, text="REGISTER", command = self.add_uname_pword).grid(row=5,column=2)

        # *** Login (Label, Entry Fields, and Button)

        Label(master, text="Login").grid(row=1,column=4)

        Label(master, text="Username").grid(row=2,column=3, sticky=E)
        self.un = Entry(master)
        self.un.grid(row=2,column=4)

        Label(master, text="Password").grid(row=3,column=3, sticky=E)
        self.pw = Entry(master, show="*")
        self.pw.grid(row=3,column=4)

        Button(master, text="LOGIN", command = self.check_uname_pword).grid(row=5,column=4)

        # *** Create Buttons (Users, Quit, and About)

        Button(master, text="USERS", command = self.users).grid(row=10,column=2)

        Button(master, text="QUIT", command = master.destroy).grid(row=10,column=3)

        Button(master, text="ABOUT", command = self.about).grid(row=10,column=4)

    # *** Method to register a username and password entered in the entry fields

    def add_uname_pword(self):
        if self.uname.get() in self.unames:
            self.User_Exists()
        else:
            if str(self.pword.get()) != str(self.pcheck.get()):
                self.Pass_No_Match()
            elif len(str(self.pword.get())) < 6:
                self.Pass_Too_Short()
            else:
                if len(self.unames) >= 10:
                    self.Too_Many_Users()
                else:
                    self.unames.append(self.uname.get())
                    self.pwords.append(self.pword.get())

                    sourceFile = open("data.csv", "a+")
                    sourceWriter = csv.DictWriter(sourceFile, fieldnames=['username', 'password'])
                    sourceWriter.writerow({'username' : self.uname.get(), 'password' : self.pword.get()})
                    sourceFile.close()

                    self.Successful_Registration()

    # *** Method to login a user using a username and password in the entry fields

    def check_uname_pword(self):
        if self.un.get() in self.unames:
            for i in range(len(self.unames)):
                if self.unames[i] == self.un.get() and self.pwords[i] == self.pw.get():
                    self.Successful_Login()
                elif self.unames[i] == self.un.get():
                    self.Wrong_Password()
        else:
            self.No_User()

    # *** Method to return a list of the currently registered usernames

    def users(self):
        win = Toplevel()
        win.wm_title("Registered Users")

        Label(win, text="Users:").grid(row=2, column=0)
        Label(win, text=str(", ".join(self.unames))).grid(row=2,column=1)
        Button(win, text="Okay", command=win.destroy).grid(row=4, column=0)

    # *** Method to return program and device information

    def about(self):
        win = Toplevel()
        win.wm_title("About Pacemaker Device Control Monitor v 1.0")

        Label(win, text="""Pacemake Device Control Monitor 1.0

              McMaster University: Department of Computing and Software
              Software Design 3K04 Fall 2018
              Ventricle Capitalists (Group 7)

              Aurora Byrdon, Arthur Faron, Yansong (Kevin) Hu, \n David Lui, Michelle Monte, Erin Puersten, Daniel Su""").grid(row=2, column=0)
        Button(win, text="Okay", command=win.destroy).grid(row=4, column=0)

    # *** Popup window methods
        
    def No_User(self):
        Popup("User not found","User not found, please try again")\

    def Wrong_Password(self):
        Popup("Password incorrect","Password incorrect, please try again")

    def Successful_Registration(self):
        Popup("Registration Successful","Successfully registered")

    def Too_Many_Users(self):
        Popup("Error","There are already 10 users registered for this program")

    def Pass_No_Match(self):
        Popup("Error","The passwords you entered do not match")

    def Pass_Too_Short(self):
        Popup("Error","Your password must be at least 6 characters long")

    def User_Exists(self):
        Popup("Error","An account already exists under this username")

    def Successful_Login(self):
        self.homeWindow = Toplevel(self.master)
        self.loginWindow = Home_Window(self.homeWindow)
    
###### HOME PAGE WINDOW

class Home_Window(Frame):
    def __init__(self,master):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Home")

        Label(master, text="Welcome Back!").grid(row=1, column=3)

        # Create Mode Selection
        
        Label(master, text="Select a Mode").grid(row = 2, column = 4, pady=3, sticky=E)
        
        modes = [ 'OFF','VOO','AOO','VVT','AAT','VVI','AAI','VDD','DOO','DDI','DDD','AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR']
        self.mode = StringVar(master)
        self.mode.set(modes[0]) 

        self.modeMenu = OptionMenu(master, self.mode, *modes, command = self.change_mode)
        self.modeMenu.grid(row = 2, column = 5, pady=3, sticky=W)

        # Create State Selection

        Label(master, text="Select a State").grid(row = 2, column = 6, pady=3, sticky=E)
        
        states = ['Permanent','Temporary','Pace-Now','Magnet','Power-On Reset']
        self.state = StringVar(master)
        self.state.set(states[0]) 
 
        self.stateMenu = OptionMenu(master, self.state, *states, command = self.change_state)
        self.stateMenu.grid(row = 2, column = 7, pady=3, sticky=W)

        # Create Label and variable entry field for Pace Rate Parameter

        Label(master, text="Pace Rate (ppm)").grid(row=3, column=2, sticky=E, pady=3)
        prates = list(range(30,51,5)) + list(range(50,91,1)) + list(range(90,176,5))
        self.pulseRate = StringVar(master)
        self.pulseRate.set('60') 
        self.pr = OptionMenu(master, self.pulseRate, *prates)
        self.pr.config(state='disabled')
        self.pr.grid(row = 3, column = 3, pady=3, sticky=W)
        
        # Create Labels and variable entry fields for AV Delay Parameters
        self.dynAVDelay = IntVar(master)
        self.davd = Checkbutton(master, text="Dynamic AV Delay", variable=self.dynAVDelay, state='disabled')
        self.davd.grid(row=5, column=2, sticky=E)
        
        Label(master, text="Fixed AV Delay (ms)").grid(row=6, column=2, sticky=E)
        favdelays = range(70,301,10)
        self.fixedAVDelay = StringVar(master)
        self.fixedAVDelay.set('150') 
        self.favd = OptionMenu(master, self.fixedAVDelay, *favdelays)
        self.favd.config(state='disabled')
        self.favd.grid(row = 6, column = 3, pady=3, sticky=W)

        Label(master, text="Sensed AV Delay Offset (ms)").grid(row=7, column=2, sticky=E)
        savdoffsets = ['OFF'] + list(range(-10,-101,-10))
        self.sensedAVDelayOffset = StringVar(master)
        self.sensedAVDelayOffset.set('OFF') 
        self.savdo = OptionMenu(master, self.sensedAVDelayOffset, *savdoffsets)
        self.savdo.config(state='disabled')
        self.savdo.grid(row = 7, column = 3, pady=3, sticky=W)

        # Create Labels and variable entry fields for Maximum Sensor Rate, Activity Threshold, Reaction Time, Response Factor, and Recovery Time
        Label(master, text="Maximum Sensor Rate (ppm)").grid(row=9, column=2, sticky=E)
        msrates = range(50,176,5)
        self.maxSensorRate = StringVar(master)
        self.maxSensorRate.set('120') 
        self.msr = OptionMenu(master, self.maxSensorRate, *msrates)
        self.msr.config(state='disabled')
        self.msr.grid(row = 9, column = 3, pady=3, sticky=W)
        
        Label(master, text="Activity Threshold").grid(row=10, column=2, sticky=E)
        thresholds = [ 'V-Low','Low','Med-Low','Med','Med-High','High','V-High']
        self.activityThreshold = StringVar(master)
        self.activityThreshold.set('Med') 
        self.at = OptionMenu(master, self.activityThreshold, *thresholds)
        self.at.config(state='disabled')
        self.at.grid(row = 10, column = 3, pady=3, sticky=W)
        
        Label(master, text="Reaction Time (sec)").grid(row=11, column=2, sticky=E)
        rtimes = range(10,51,10)
        self.reactionTime = StringVar(master)
        self.reactionTime.set('30') 
        self.ret = OptionMenu(master, self.reactionTime, *rtimes)
        self.ret.config(state='disabled')
        self.ret.grid(row = 11, column = 3, pady=3, sticky=W)

        Label(master, text="Response Factor").grid(row=12, column=2, sticky=E)
        rfactors = range(1,17)
        self.responseFactor = StringVar(master)
        self.responseFactor.set('8') 
        self.rf = OptionMenu(master, self.responseFactor, *rfactors)
        self.rf.config(state='disabled')
        self.rf.grid(row = 12, column = 3, pady=3, sticky=W)

        Label(master, text="Recovery Time (min)").grid(row=13, column=2, sticky=E)
        rtimes = range(2,17)
        self.recoveryTime = StringVar(master)
        self.recoveryTime.set('5') 
        self.rt = OptionMenu(master, self.recoveryTime, *rtimes)
        self.rt.config(state='disabled')
        self.rt.grid(row = 13, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for ventricular parameters
        Label(master, text="Ventricular Pulse Width (ms)").grid(row=3, column=4, sticky=E)
        venpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        self.vPulseWidth = StringVar(master)
        self.vPulseWidth.set(0.4) 
        self.vpw = OptionMenu(master, self.vPulseWidth, *venpws)
        self.vpw.config(state='disabled')
        self.vpw.grid(row = 3, column = 5, pady=3, sticky=W)

        Label(master, text="Ventricular Amplitude (V)").grid(row=4, column=4, sticky=E, pady=3)
        vas = ['0.00','1.25','2.50','3.75','5.00']
        self.vAmp = StringVar(master)
        self.vAmp.set(3.75) 
        self.va = OptionMenu(master, self.vAmp, *vas)
        self.va.config(state='disabled')
        self.va.grid(row = 4, column = 5, pady=3, sticky=W)

        Label(master, text="Ventricular Sensitivity (mV)").grid(row=5, column=4, sticky=E)
        vsens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.vSensitivity = StringVar(master)
        self.vSensitivity.set(2.5) 
        self.vs = OptionMenu(master, self.vSensitivity, *vsens)
        self.vs.config(state='disabled')
        self.vs.grid(row = 5, column = 5, pady=3, sticky=W)

        # Create labels and variable entry fields for refractory period parameters
        Label(master, text="VRP (ms)").grid(row=7, column=4, sticky=E)
        vrpvars = range(150,501,10)
        self.vRefractPeriod = StringVar(master)
        self.vRefractPeriod.set(320) 
        self.vrp = OptionMenu(master, self.vRefractPeriod, *vrpvars)
        self.vrp.config(state='disabled')
        self.vrp.grid(row = 7, column = 5, pady=3, sticky=W)
        
        Label(master, text="ARP (ms)").grid(row=8, column=4, sticky=E)
        arpvars = range(150,501,10)
        self.aRefractPeriod = StringVar(master)
        self.aRefractPeriod.set(250) 
        self.arp = OptionMenu(master, self.aRefractPeriod, *arpvars)
        self.arp.config(state='disabled')
        self.arp.grid(row = 8, column = 5, pady=3, sticky=W)

        Label(master, text="PVARP (ms)").grid(row=9, column=4, sticky=E)
        pvarpvars = range(150,501,10)
        self.postVARefractPeriod = StringVar(master)
        self.postVARefractPeriod.set(250) 
        self.pvarp = OptionMenu(master, self.postVARefractPeriod, *pvarpvars)
        self.pvarp.config(state='disabled')
        self.pvarp.grid(row = 9, column = 5, pady=3, sticky=W)

        Label(master, text="PVARP Extension (ms)").grid(row=10, column=4, sticky=E)
        pvarpevars = ['OFF'] + list(range(50,401,50))
        self.postVARefractPeriodExt = StringVar(master)
        self.postVARefractPeriodExt.set('OFF') 
        self.pvarpe = OptionMenu(master, self.postVARefractPeriodExt, *pvarpevars)
        self.pvarpe.config(state='disabled')
        self.pvarpe.grid(row = 10, column = 5, pady=3, sticky=W)

        # Create labels and variable entry fields for atrial parameters
        Label(master, text="Atrial Pulse Width (ms)").grid(row=3, column=6, sticky=E, pady=3)
        atrpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        self.aPulseWidth = StringVar(master)
        self.aPulseWidth.set(0.4) 
        self.apw = OptionMenu(master, self.aPulseWidth, *atrpws)
        self.apw.config(state='disabled')
        self.apw.grid(row = 3, column = 7, pady=3, sticky=W)

        Label(master, text="Atrial Amplitude (V)").grid(row=4, column=6, sticky=E)
        aas = ['0.00','1.25','2.50','3.75','5.00']
        self.aAmp = StringVar(master)
        self.aAmp.set(3.75) 
        self.aa = OptionMenu(master, self.aAmp, *aas)
        self.aa.config(state='disabled')
        self.aa.grid(row = 4, column = 7, pady=3, sticky=W)

        Label(master, text="Atrial Sensitivity (mV)").grid(row=5, column=6, sticky=E)
        asens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.aSensitivity = StringVar(master)
        self.aSensitivity.set(0.75) 
        self.ase = OptionMenu(master, self.aSensitivity, *asens)
        self.ase.config(state='disabled')
        self.ase.grid(row = 5, column = 7, pady=3, sticky=W)

        # Create labels and variable entry fields for rate smoothing, hysteresis, and atr settings
        Label(master, text="Rate Smoothing (%)").grid(row=7, column=6, sticky=E)
        rsmooths = [ 'Off','3','6','9','12','15','18','21','25']
        self.rateSmoothing = StringVar(master)
        self.rateSmoothing.set('Off') 
        self.rs = OptionMenu(master, self.rateSmoothing, *rsmooths)
        self.rs.config(state='disabled')
        self.rs.grid(row = 7, column = 7, pady=3, sticky=W)

        Label(master, text="Hysteresis (ppm)").grid(row=8, column=6, sticky=E)
        hysrates = [ 'Off'] + list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        self.hys = StringVar(master)
        self.hys.set('Off') 
        self.h = OptionMenu(master, self.hys, *hysrates)
        self.h.config(state='disabled')
        self.h.grid(row = 8, column = 7, pady=3, sticky=W)
        
        self.atrfm = Checkbutton(master, text="ATR Fallback Mode", variable=IntVar(), state='disabled')
        self.atrfm.grid(row=10, column=6, sticky=E)

        Label(master, text="ATR Duration (cc)").grid(row=11, column=6, sticky=E)
        atrdurs = [10] + list(range(20,81,20)) + list(range(100, 2001,100))
        self.atrDuration = StringVar(master)
        self.atrDuration.set('20') 
        self.atrd = OptionMenu(master, self.atrDuration, *atrdurs)
        self.atrd.config(state='disabled')
        self.atrd.grid(row = 11, column = 7, pady=3, sticky=W)

        Label(master, text="ATR Fallback Time (min)").grid(row=12, column=6, sticky=E)
        ftimes = range(1,6)
        self.atrFallbackTime = StringVar(master)
        self.atrFallbackTime.set('1') 
        self.atrft = OptionMenu(master, self.atrFallbackTime, *ftimes)
        self.atrft.config(state='disabled')
        self.atrft.grid(row = 12, column = 7, pady=3, sticky=W)

        # Create buttons to Send Parameters, Change Patients, get More Information, Start/Stop Egram Transmission
        Button(master, text="More Information", command=self.More_Info).grid(row=12, column=4)
        Button(master, text="Send Parameters", command=self.Send_Param).grid(row=13, column=4)
        Button(master, text="QUIT", command = master.destroy).grid(row=14,column=4)
        Button(master, text="Change Patients", command=master.destroy).grid(row=12, column=5)
        Button(master, text="Start Egram Transmission", command=self.Start_Egram).grid(row=13, column=5)
        
    # Method to change the mode - parameters are greyed out accordingly
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

    def change_state(self,state):
        if state == 'Permanent':
            self.modeMenu.config(state='normal')
        else:
            self.change_mode('OFF')
            self.mode.set('OFF')
            self.modeMenu.config(state='disable')
            
        #### Will need to incorporate additional states if necessary (at the moment, only 'Permanent' is enabled

        
    # Method to send (print at the moment) the set parameters    
    def Send_Param(self):
        Popup("Parameter Transmission","Parameters are being transmitted to the Pacemaker")
        print(self.mode.get())
        if self.mode.get() == "VOO":
            print("Pulse Rate: " + self.pulseRate.get() + "ppm")
            print("Ventricular Amplitude: " + self.vAmp.get() + "V")
            print("Ventricular Pulse Width: " + self.vPulseWidth.get() + "mV")
        #### Will need to use serial communication to send parameters to the board
        #### Will need to write code which will send all parameters for each new mode to the board

    # Method to request more info on the parameters
    def More_Info(self):
        Popup("Mode and Parameter Information","""Start by selecting a mode and a state

            Modes:
              (1) First Character - Chambers Paced:  V = Ventricular   A = Atrial   D = Dual Chamber   O = None
              (2) Second Character - Chambers Sensed:  V = Ventricular   A = Atrial   D = Dual Chamber   O = None
              (3) Third Character - Response to Sensing:   O = None   T = Triggered   I = Inhibited   D = Tracked
              (4) Fourth Character - Rate Modulation:   R = Rate Modulation (optional)

            States:
               Permanent State - the state of normal operation of the pacing device, all modes are available
               Temporary State - a temporary state of pacing (currently unavailable)
               Pace-Now State - a state of emergency bradycardia pacing where the mode is set to VVI and the parameters are set to preset values (currently unavailable)
               Magnet State - a state used to determine the battery status of the device (currently unavailable)
               Power-On Reset State - a state entered when the battery drops too low (currently unavailable)

            Depending on the mode and state selected certain parameters will become available to set""")

    # Methods to request and stop transmission of Egram data 
    def Start_Egram(self):
        self.egramWindow = Toplevel(self.master)
        self.loginWindow = Egram_Window(self.egramWindow)
        #### Will need to use serial communication to gather egram data from the board

class Egram_Window(Frame):
    def __init__(self,master):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Electrogram Viewer")

        Label(master, text="Electrogram Here!").grid(row=1, column=1)

        Button(master, text="QUIT", command = master.destroy).grid(row=2,column=1)

        #### Will need to display egram data graphically
        #### Will need to use serial communication to halt egram data from the board
    
root = Tk()
loginWindow = Login_Window(root)
root.mainloop()
