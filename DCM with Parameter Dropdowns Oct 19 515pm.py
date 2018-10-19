### TO DO
# tidy up the code
# when the home window (parameter and mode) is opened, the login window should close
# when change patient is select, the login window should reopen and the home window should close
# new page for egram data (blank page for now) with stop transmission button on this page
# press random key and brin up device detected window (asks would you like to interrogate the device)
# states should impact the modes available (e.g. some states only allow vvi mode)

### PARAMETERS
# fill in more information page
# some parameters are only available if a checkbox is ticked - grey them out if the checkbox is not ticked
# add minimum dynamic av delay and ventricular blanking???

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

        self.register = Button(master, text="REGISTER", command = self.add_uname_pword)
        self.register.grid(row=5,column=2)

        # *** Login

        Label(master, text="Login").grid(row=1,column=4)

        Label(master, text="Username").grid(row=2,column=3, sticky=E)
        self.un = Entry(master)
        self.un.grid(row=2,column=4)

        Label(master, text="Password").grid(row=3,column=3, sticky=E)
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
        root = Tk()
        home = Home_Window(root)
        root.mainloop()

##### POPUP WINDOW DEFINITION

def Popup(popup_title,popup_description):
    win = Toplevel()
    win.wm_title(popup_title)

    l = Label(win, text=popup_description)
    l.grid(row=2, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b.grid(row=3, column=0)
    
###### HOME PAGE WINDOW

class Home_Window(Frame):
    def __init__(self,master):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Home")

        Label(master, text="Welcome Back!").grid(row=1, column=3)

        # Selecting a Mode
        
        Label(master, text="Select a Mode").grid(row = 2, column = 4, pady=3, sticky=E)
        
        modes = [ 'OFF','VOO','AOO','VVT','AAT','VVI','AAI','VDD','DOO','DDI','DDD','AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR']
        mode = StringVar(master)
        mode.set(modes[0]) 
 
        self.modeMenu = OptionMenu(master, mode, *modes, command = self.change_mode)
        self.modeMenu.grid(row = 2, column = 5, pady=3, sticky=W)

        # Selecting a State

        Label(master, text="Select a State").grid(row = 2, column = 6, pady=3, sticky=E)
        
        states = [ 'Off','Permanent','Temporary','Pace-Now','Magnet','Power-On Reset']
        state = StringVar(master)
        state.set(states[0]) # set the default option
 
        self.stateMenu = OptionMenu(master, state, *states, command = self.change_state)
        self.stateMenu.grid(row = 2, column = 7, pady=3, sticky=W)

        # Create Label and variable entry field for Pace Rate Parameter

        Label(master, text="Pace Rate (ppm)").grid(row=3, column=2, sticky=E, pady=3)
        prates = list(range(30,51,5)) + list(range(50,91,1)) + list(range(90,176,5))
        prate = StringVar(master)
        prate.set('60') 
        self.pr = OptionMenu(master, prate, *prates)
        self.pr.config(state='disabled')
        self.pr.grid(row = 3, column = 3, pady=3, sticky=W)
        
        # Create Labels and variable entry fields for AV Delay Parameters
        self.davd = Checkbutton(master, text="Dynamic AV Delay", variable=IntVar(),state='disabled')
        self.davd.grid(row=5, column=2, sticky=E)
        
        Label(master, text="Fixed AV Delay (ms)").grid(row=6, column=2, sticky=E)
        favdelays = range(70,301,10)
        favdelay = StringVar(master)
        favdelay.set('150') 
        self.favd = OptionMenu(master, favdelay, *favdelays)
        self.favd.config(state='disabled')
        self.favd.grid(row = 6, column = 3, pady=3, sticky=W)

        Label(master, text="Sensed AV Delay Offset (ms)").grid(row=7, column=2, sticky=E)
        savdoffsets = ['OFF'] + list(range(-10,-101,-10))
        savdoffset = StringVar(master)
        savdoffset.set('OFF') 
        self.savdo = OptionMenu(master, savdoffset, *savdoffsets)
        self.savdo.config(state='disabled')
        self.savdo.grid(row = 7, column = 3, pady=3, sticky=W)

        # Create Labels and variable entry fields for Maximum Sensor Rate, Activity Threshold, Reaction Time, Response Factor, and Recovery Time
        Label(master, text="Maximum Sensor Rate (ppm)").grid(row=9, column=2, sticky=E)
        msrates = range(50,176,5)
        msrate = StringVar(master)
        msrate.set('120') 
        self.msr = OptionMenu(master, msrate, *msrates)
        self.msr.config(state='disabled')
        self.msr.grid(row = 9, column = 3, pady=3, sticky=W)
        
        Label(master, text="Activity Threshold").grid(row=10, column=2, sticky=E)
        thresholds = [ 'V-Low','Low','Med-Low','Med','Med-High','High','V-High']
        threshold = StringVar(master)
        threshold.set('Med') 
        self.at = OptionMenu(master, threshold, *thresholds)
        self.at.config(state='disabled')
        self.at.grid(row = 10, column = 3, pady=3, sticky=W)
        
        Label(master, text="Reaction Time (sec)").grid(row=11, column=2, sticky=E)
        rtimes = range(10,51,10)
        rtime = StringVar(master)
        rtime.set('30') 
        self.ret = OptionMenu(master, rtime, *rtimes)
        self.ret.config(state='disabled')
        self.ret.grid(row = 11, column = 3, pady=3, sticky=W)

        Label(master, text="Response Factor").grid(row=12, column=2, sticky=E)
        rfactors = range(1,17)
        rfactor = StringVar(master)
        rfactor.set('8') 
        self.rf = OptionMenu(master, rfactor, *rfactors)
        self.rf.config(state='disabled')
        self.rf.grid(row = 12, column = 3, pady=3, sticky=W)

        Label(master, text="Recovery Time (min)").grid(row=13, column=2, sticky=E)
        rtimes = range(2,17)
        rtime = StringVar(master)
        rtime.set('5') 
        self.rt = OptionMenu(master, rtime, *rtimes)
        self.rt.config(state='disabled')
        self.rt.grid(row = 13, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for ventricular parameters
        Label(master, text="Ventricular Pulse Width (ms)").grid(row=3, column=4, sticky=E)
        venpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        venpw = StringVar(master)
        venpw.set(0.4) 
        self.vpw = OptionMenu(master, venpw, *venpws)
        self.vpw.config(state='disabled')
        self.vpw.grid(row = 3, column = 5, pady=3, sticky=W)

        Label(master, text="Ventricular Amplitude (V)").grid(row=4, column=4, sticky=E, pady=3)
        vas = ['0.00','1.25','2.50','3.75','5.00']
        va = StringVar(master)
        va.set(3.75) 
        self.va = OptionMenu(master, va, *vas)
        self.va.config(state='disabled')
        self.va.grid(row = 4, column = 5, pady=3, sticky=W)

        Label(master, text="Ventricular Sensitivity (mV)").grid(row=5, column=4, sticky=E)
        vsens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        vsen = StringVar(master)
        vsen.set(2.5) 
        self.vs = OptionMenu(master, vsen, *vsens)
        self.vs.config(state='disabled')
        self.vs.grid(row = 5, column = 5, pady=3, sticky=W)

        # Create labels and variable entry fields for refractory period parameters
        Label(master, text="VRP (ms)").grid(row=7, column=4, sticky=E)
        vrpvars = range(150,501,10)
        vrpvar = StringVar(master)
        vrpvar.set(320) 
        self.vrp = OptionMenu(master, vrpvar, *vrpvars)
        self.vrp.config(state='disabled')
        self.vrp.grid(row = 7, column = 5, pady=3, sticky=W)
        
        Label(master, text="ARP (ms)").grid(row=8, column=4, sticky=E)
        arpvars = range(150,501,10)
        arpvar = StringVar(master)
        arpvar.set(250) 
        self.arp = OptionMenu(master, arpvar, *arpvars)
        self.arp.config(state='disabled')
        self.arp.grid(row = 8, column = 5, pady=3, sticky=W)

        Label(master, text="PVARP (ms)").grid(row=9, column=4, sticky=E)
        pvarpvars = range(150,501,10)
        pvarpvar = StringVar(master)
        pvarpvar.set(250) 
        self.pvarp = OptionMenu(master, pvarpvar, *pvarpvars)
        self.pvarp.config(state='disabled')
        self.pvarp.grid(row = 9, column = 5, pady=3, sticky=W)

        Label(master, text="PVARP Extension (ms)").grid(row=10, column=4, sticky=E)
        pvarpevars = ['OFF'] + list(range(50,401,50))
        pvarpevar = StringVar(master)
        pvarpevar.set('OFF') 
        self.pvarpe = OptionMenu(master, pvarpevar, *pvarpevars)
        self.pvarpe.config(state='disabled')
        self.pvarpe.grid(row = 10, column = 5, pady=3, sticky=W)

        # Create labels and variable entry fields for atrial parameters
        Label(master, text="Atrial Pulse Width (ms)").grid(row=3, column=6, sticky=E, pady=3)
        atrpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        atrpw = StringVar(master)
        atrpw.set(0.4) 
        self.apw = OptionMenu(master, atrpw, *atrpws)
        self.apw.config(state='disabled')
        self.apw.grid(row = 3, column = 7, pady=3, sticky=W)

        Label(master, text="Atrial Amplitude (V)").grid(row=4, column=6, sticky=E)
        aas = ['0.00','1.25','2.50','3.75','5.00']
        aa = StringVar(master)
        aa.set(3.75) 
        self.aa = OptionMenu(master, aa, *aas)
        self.aa.config(state='disabled')
        self.aa.grid(row = 4, column = 7, pady=3, sticky=W)

        Label(master, text="Atrial Sensitivity (mV)").grid(row=5, column=6, sticky=E)
        asens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        asen = StringVar(master)
        asen.set(0.75) 
        self.ase = OptionMenu(master, asen, *asens)
        self.ase.config(state='disabled')
        self.ase.grid(row = 5, column = 7, pady=3, sticky=W)

        # Create labels and variable entry fields for rate smoothing, hysteresis, and atr settings
        Label(master, text="Rate Smoothing (%)").grid(row=7, column=6, sticky=E)
        rsmooths = [ 'Off','3','6','9','12','15','18','21','25']
        rsmooth = StringVar(master)
        rsmooth.set('Off') 
        self.rs = OptionMenu(master, rsmooth, *rsmooths)
        self.rs.config(state='disabled')
        self.rs.grid(row = 7, column = 7, pady=3, sticky=W)

        Label(master, text="Hysteresis (ppm)").grid(row=8, column=6, sticky=E)
        hysrates = [ 'Off'] + list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        hys = StringVar(master)
        hys.set('Off') 
        self.h = OptionMenu(master, hys, *hysrates)
        self.h.config(state='disabled')
        self.h.grid(row = 8, column = 7, pady=3, sticky=W)
        
        self.atrfm = Checkbutton(master, text="ATR Fallback Mode", variable=IntVar(), state='disabled')
        self.atrfm.grid(row=10, column=6, sticky=E)

        Label(master, text="ATR Duration (cc)").grid(row=11, column=6, sticky=E)
        atrdurs = [10] + list(range(20,81,20)) + list(range(100, 2001,100))
        atrdur = StringVar(master)
        atrdur.set('20') 
        self.atrd = OptionMenu(master, atrdur, *atrdurs)
        self.atrd.config(state='disabled')
        self.atrd.grid(row = 11, column = 7, pady=3, sticky=W)

        Label(master, text="ATR Fallback Time (min)").grid(row=12, column=6, sticky=E)
        ftimes = range(1,6)
        ftime = StringVar(master)
        ftime.set('1') 
        self.atrft = OptionMenu(master, ftime, *ftimes)
        self.atrft.config(state='disabled')
        self.atrft.grid(row = 12, column = 7, pady=3, sticky=W)

        # Create buttons for Home Menu
        transmit_param = Button(master, text="Send Parameters", command=self.Send_Param)
        transmit_param.grid(row=13, column=4)

        new_patient = Button(master, text="Change Patients", command=master.destroy)
        ### At the moment this only destroys the window, we need it to also repen the login window
        new_patient.grid(row=12, column=5)

        more_info = Button(master, text="More Information", command=self.More_Info)
        more_info.grid(row=12, column=4)

        more_info = Button(master, text="Start Egram Transmission", command=self.Start_Egram)
        more_info.grid(row=13, column=5)

        more_info = Button(master, text="Stop Egram Transmission", command=self.Stop_Egram)
        more_info.grid(row=14, column=5)

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
        print(state)
        # Will need to change the modes accordingly
        # Pace-Now specifies VVI mode with specific parameters
        # Permanent State should allow all modes
        # Temporary Mode is not clear
        # Magnet state is used during the magnet test
        # POR state is very similar to Pace-Now
            
    def Send_Param(self):
        Popup("Parameter Transmission","Parameters are being transmitted to the Pacemaker")
        # Will need to actually use serial communication to send parameters to the board

    def More_Info(self):
        Popup("Mode and Parameter Information","This is the information")

    def Start_Egram(self):
        Popup("Egram Data Request", "Egram data transmission has been requested and is in progress")
        # Will need to actually use serial communication to gather egram data from the board

    def Stop_Egram(self):
        Popup("Egram Data Cancellation Request", "Egram data transmission has been requested to cancel and is in progress")
        # Will need to use serial communication to halt egram data from the board

    
root = Tk()
my_window = Login_Window(root)
root.mainloop()
