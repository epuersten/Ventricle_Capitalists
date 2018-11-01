import tkinter
from tkinter import *
from _LoginWindow import *
from _EgramWindow import *

#Home Window.

class Home_Window(Frame):
    def __init__(self,master):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Home")

        Label(master, text="Welcome Back!").grid(row=2, column=2)

        Label(master, text="BASIC PARAMETERS: ").grid(row=4, column=2)

        Label(master,text="ADV. PARAMETERS: ").grid(row=8,column=2)

        # Create buttons to Send Parameters, Change Patients, get More Information, Start/Stop Egram Transmission
        Button(master, text="MORE INFORMATION", command=self.__more_info).grid(row=1, column=2)
        Button(master, text="START EGRAM TRANSMISSION", command=self.__start_egram).grid(row=1, column=5)
        Button(master, text="SEND PARAMETERS", command=self.__send_param).grid(row=1, column=3)
        Button(master, text="CHANGE PATIENTS", command=master.destroy).grid(row=1, column=6)
        Button(master, text="QUIT", command = master.destroy).grid(row=1,column=9)

        # Create Mode Selection
        
        Label(master, text="Select a Mode").grid(row = 3, column = 2, pady=3, sticky=E)
        
        modes = [ 'OFF','VOO','AOO','VVT','AAT','VVI','AAI','VDD','DOO','DDI','DDD','AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR']
        self.mode = StringVar(master)
        self.mode.set(modes[0]) 

        self.modeMenu = OptionMenu(master, self.mode, *modes, command = self.__change_mode)
        self.modeMenu.grid(row = 3, column = 3, pady=3, sticky=W)

        # Create State Selection

        Label(master, text="Select a State").grid(row = 3, column = 5, pady=3, sticky=E)
        
        states = ['Permanent','Temporary','Pace-Now','Magnet','Power-On Reset']
        self.state = StringVar(master)
        self.state.set(states[0]) 
 
        self.stateMenu = OptionMenu(master, self.state, *states, command = self.__change_state)
        self.stateMenu.grid(row = 3, column = 6, pady=3, sticky=W)

        # Create label and variable entry field for Pace Rate Parameter

        Label(master, text="Upper Pace Rate (ppm)").grid(row=5, column=2, sticky=E, pady=3)
        uprates = list(range(50,176,5))
        self.upperPulseRate = StringVar(master)
        self.upperPulseRate.set('120') 
        self.upr = OptionMenu(master, self.upperPulseRate, *uprates)
        self.upr.config(state='disabled', bg='LIGHTGRAY')
        self.upr.grid(row = 5, column = 3, pady=3, sticky=W)

        Label(master, text="Lower Pace Rate (ppm)").grid(row=6, column=2, sticky=E, pady=3)
        lprates = list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        self.lowerPulseRate = StringVar(master)
        self.lowerPulseRate.set('60') 
        self.lpr = OptionMenu(master, self.lowerPulseRate, *lprates)
        self.lpr.config(state='disabled', bg='LIGHTGRAY')
        self.lpr.grid(row = 6, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for ventricular parameters
        Label(master, text="Ventricular Pulse Width (ms)").grid(row=5, column=5, sticky=E)
        venpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        self.vPulseWidth = StringVar(master)
        self.vPulseWidth.set(0.4) 
        self.vpw = OptionMenu(master, self.vPulseWidth, *venpws)
        self.vpw.config(state='disabled', bg='LIGHTGREY')
        self.vpw.grid(row = 5, column = 6, pady=3, sticky=W)

        Label(master, text="Ventricular Amplitude (V)").grid(row=6, column=5, sticky=E, pady=3)
        vas = ['0.00','1.25','2.50','3.75','5.00']
        self.vAmp = StringVar(master)
        self.vAmp.set(3.75) 
        self.va = OptionMenu(master, self.vAmp, *vas)
        self.va.config(state='disabled', bg='LIGHTGREY')
        self.va.grid(row = 6, column = 6, pady=3, sticky=W)

        Label(master, text="Ventricular Sensitivity (mV)").grid(row=7, column=5, sticky=E)
        vsens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.vSensitivity = StringVar(master)
        self.vSensitivity.set(2.5) 
        self.vs = OptionMenu(master, self.vSensitivity, *vsens)
        self.vs.config(state='disabled', bg='LIGHTGREY')
        self.vs.grid(row = 7, column = 6, pady=3, sticky=W)

        # Create labels and variable entry fields for atrial parameters
        Label(master, text="Atrial Pulse Width (ms)").grid(row=5, column=8, sticky=E, pady=3)
        atrpws = ['0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9']
        self.aPulseWidth = StringVar(master)
        self.aPulseWidth.set(0.4) 
        self.apw = OptionMenu(master, self.aPulseWidth, *atrpws)
        self.apw.config(state='disabled', bg='LIGHTGREY')
        self.apw.grid(row = 5, column = 9, pady=3, sticky=W)

        Label(master, text="Atrial Amplitude (V)").grid(row=6, column=8, sticky=E)
        aas = ['0.00','1.25','2.50','3.75','5.00']
        self.aAmp = StringVar(master)
        self.aAmp.set(3.75) 
        self.aa = OptionMenu(master, self.aAmp, *aas)
        self.aa.config(state='disabled', bg='LIGHTGREY')
        self.aa.grid(row = 6, column = 9, pady=3, sticky=W)

        Label(master, text="Atrial Sensitivity (mV)").grid(row=7, column=8, sticky=E)
        asens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.aSensitivity = StringVar(master)
        self.aSensitivity.set(0.75) 
        self.ase = OptionMenu(master, self.aSensitivity, *asens)
        self.ase.config(state='disabled', bg='LIGHTGREY')
        self.ase.grid(row = 7, column = 9, pady=3, sticky=W)

        # Create labels and entry fields for ATR parameters
        self.atrOn = IntVar()
        self.atrfm = Checkbutton(master, text="ATR Fallback Mode", variable=self.atrOn, state='disabled', command = self.__enable_atr)
        self.atrfm.grid(row=9, column=2, sticky=W)

        Label(master, text="ATR Duration (cc)").grid(row=10, column=2, sticky=E)
        atrdurs = [10] + list(range(20,81,20)) + list(range(100, 2001,100))
        self.atrDuration = StringVar(master)
        self.atrDuration.set('20') 
        self.atrd = OptionMenu(master, self.atrDuration, *atrdurs)
        self.atrd.config(state='disabled', bg='LIGHTGREY')
        self.atrd.grid(row = 10, column = 3, pady=3, sticky=W)

        Label(master, text="ATR Fallback Time (min)").grid(row=11, column=2, sticky=E)
        ftimes = range(1,6)
        self.atrFallbackTime = StringVar(master)
        self.atrFallbackTime.set('1') 
        self.atrft = OptionMenu(master, self.atrFallbackTime, *ftimes)
        self.atrft.config(state='disabled', bg='LIGHTGREY')
        self.atrft.grid(row = 11, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for Rate Smoothing and Hysteresis
        self.rateSmoothOn = IntVar()
        self.rsOn = Checkbutton(master, text="Rate Smoothing", variable=self.rateSmoothOn, state='disabled', command = self.__enable_rs)
        self.rsOn.grid(row=9, column=5, sticky=W)

        Label(master, text="Rate Smoothing (%)").grid(row=10, column=5, sticky=E)
        rsmooths = list(range(3,24,3)) + [25]
        self.rateSmoothing = StringVar(master)
        self.rateSmoothing.set('3') 
        self.rs = OptionMenu(master, self.rateSmoothing, *rsmooths)
        self.rs.config(state='disabled', bg='LIGHTGREY')
        self.rs.grid(row = 10, column = 6, pady=6, sticky=W)

        self.hysOn = IntVar()
        self.hOn = Checkbutton(master, text="Hysteresis", variable=self.hysOn, state='disabled', command = self.__enable_hys)
        self.hOn.grid(row=11, column=5, sticky=W)

        Label(master, text="Hysteresis Rate (ppm)").grid(row=12, column=5, sticky=E)
        hysrates = list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        self.hys = StringVar(master)
        self.hys.set('60') 
        self.h = OptionMenu(master, self.hys, *hysrates)
        self.h.config(state='disabled', bg='LIGHTGREY')
        self.h.grid(row = 12, column = 6, pady=6, sticky=W)

        # Create labels and variable entry fields for refractory period parameters
        Label(master, text="VRP (ms)").grid(row=9, column=8, sticky=E)
        vrpvars = range(150,501,10)
        self.vRefractPeriod = StringVar(master)
        self.vRefractPeriod.set(320) 
        self.vrp = OptionMenu(master, self.vRefractPeriod, *vrpvars)
        self.vrp.config(state='disabled', bg='LIGHTGREY')
        self.vrp.grid(row = 9, column = 9, pady=3, sticky=W)
        
        Label(master, text="ARP (ms)").grid(row=10, column=8, sticky=E)
        arpvars = range(150,501,10)
        self.aRefractPeriod = StringVar(master)
        self.aRefractPeriod.set(250) 
        self.arp = OptionMenu(master, self.aRefractPeriod, *arpvars)
        self.arp.config(state='disabled', bg='LIGHTGREY')
        self.arp.grid(row = 10, column = 9, pady=3, sticky=W)

        Label(master, text="PVARP (ms)").grid(row=11, column=8, sticky=E)
        pvarpvars = range(150,501,10)
        self.postVARefractPeriod = StringVar(master)
        self.postVARefractPeriod.set(250) 
        self.pvarp = OptionMenu(master, self.postVARefractPeriod, *pvarpvars)
        self.pvarp.config(state='disabled', bg='LIGHTGREY')
        self.pvarp.grid(row = 11, column = 9, pady=3, sticky=W)

        self.postVARPExtOn = IntVar()
        self.pvarpeOn = Checkbutton(master, text="PVARP Extension", variable=self.postVARPExtOn, state='disabled', command = self.__enable_pvarpe)
        self.pvarpeOn.grid(row=12, column=8, sticky=W)

        Label(master, text="PVARP Extension (ms)").grid(row=13, column=8, sticky=E)
        pvarpevars = range(50,401,50)
        self.postVARefractPeriodExt = StringVar(master)
        self.postVARefractPeriodExt.set('50') 
        self.pvarpe = OptionMenu(master, self.postVARefractPeriodExt, *pvarpevars)
        self.pvarpe.config(state='disabled', bg='LIGHTGREY')
        self.pvarpe.grid(row = 13, column = 9, pady=3, sticky=W)
        
        # Create labels and variable entry fields for AV Delay Parameters
        self.dynAVDelay = IntVar()
        self.davd = Checkbutton(master, text="Dynamic AV Delay", variable=self.dynAVDelay, state='disabled')
        self.davd.grid(row=14, column=5, sticky=W)
        
        Label(master, text="Fixed AV Delay (ms)").grid(row=15, column=5, sticky=E)
        favdelays = range(70,301,10)
        self.fixedAVDelay = StringVar(master)
        self.fixedAVDelay.set('150') 
        self.favd = OptionMenu(master, self.fixedAVDelay, *favdelays)
        self.favd.config(state='disabled', bg='LIGHTGREY')
        self.favd.grid(row =15, column = 6, pady=3, sticky=W)

        self.savdOffsetOn = IntVar()
        self.savdoOn = Checkbutton(master, text="Sensed AV Delay Offset", variable=self.savdOffsetOn, state='disabled', command = self.__enable_savdo)
        self.savdoOn.grid(row=16, column=5, sticky=W)

        Label(master, text="Sensed AV Delay Offset (ms)").grid(row=17, column=5, sticky=E)
        savdoffsets = list(range(-10,-101,-10))
        self.sensedAVDelayOffset = StringVar(master)
        self.sensedAVDelayOffset.set('-10') 
        self.savdo = OptionMenu(master, self.sensedAVDelayOffset, *savdoffsets)
        self.savdo.config(state='disabled', bg='LIGHTGREY')
        self.savdo.grid(row = 17, column = 6, pady=3, sticky=W)

        # Create labels and variable entry fields for Maximum Sensor Rate, Activity Threshold, Reaction Time, Response Factor, and Recovery Time        
        Label(master, text="Activity Threshold").grid(row=13, column=2, sticky=E)
        thresholds = [ 'V-Low','Low','Med-Low','Med','Med-High','High','V-High']
        self.activityThreshold = StringVar(master)
        self.activityThreshold.set('Med') 
        self.at = OptionMenu(master, self.activityThreshold, *thresholds)
        self.at.config(state='disabled', bg='LIGHTGREY')
        self.at.grid(row = 13, column = 3, pady=3, sticky=W)
        
        Label(master, text="Reaction Time (sec)").grid(row=14, column=2, sticky=E)
        rtimes = range(10,51,10)
        self.reactionTime = StringVar(master)
        self.reactionTime.set('30') 
        self.ret = OptionMenu(master, self.reactionTime, *rtimes)
        self.ret.config(state='disabled', bg='LIGHTGREY')
        self.ret.grid(row = 14, column = 3, pady=3, sticky=W)

        Label(master, text="Response Factor").grid(row=15, column=2, sticky=E)
        rfactors = range(1,17)
        self.responseFactor = StringVar(master)
        self.responseFactor.set('8') 
        self.rf = OptionMenu(master, self.responseFactor, *rfactors)
        self.rf.config(state='disabled', bg='LIGHTGREY')
        self.rf.grid(row = 15, column = 3, pady=3, sticky=W)

        Label(master, text="Recovery Time (min)").grid(row=16, column=2, sticky=E)
        rtimes = range(2,17)
        self.recoveryTime = StringVar(master)
        self.recoveryTime.set('5') 
        self.rt = OptionMenu(master, self.recoveryTime, *rtimes)
        self.rt.config(state='disabled', bg='LIGHTGREY')
        self.rt.grid(row = 16, column = 3, pady=3, sticky=W)

        Label(master, text="Maximum Sensor Rate (ppm)").grid(row=17, column=2, sticky=E)
        msrates = range(50,176,5)
        self.maxSensorRate = StringVar(master)
        self.maxSensorRate.set('120') 
        self.msr = OptionMenu(master, self.maxSensorRate, *msrates)
        self.msr.config(state='disabled', bg='LIGHTGREY')
        self.msr.grid(row = 17, column = 3, pady=3, sticky=W)

        # Method to change the mode - parameters are LIGHTGREYed out accordingly
    def __change_mode(self,mode):
        # if the mode is off - do not allow user to set anything
        if mode == 'OFF':
            self.hOn.deselect()
            self.__enable_hys()
            self.hOn.config(state='disabled')
            self.rsOn.deselect()
            self.__enable_rs()
            self.rsOn.config(state='disabled')

            self.atrfm.deselect()
            self.__enable_atr()
            self.atrfm.config(state='disabled')

            self.vrp.config(state='disabled', bg='LIGHTGREY')
            self.arp.config(state='disabled', bg='LIGHTGREY')
            self.pvarp.config(state='disabled', bg='LIGHTGREY')
            self.pvarpeOn.deselect()
            self.__enable_pvarpe()
            self.pvarpeOn.config(state='disabled')

            self.favd.config(state='disabled', bg='LIGHTGREY')
            self.davd.config(state='disabled')
            self.savdoOn.deselect()
            self.__enable_savdo()
            self.savdoOn.config(state='disabled')
            
            self.upr.config(state='disabled', bg='LIGHTGREY')
            self.lpr.config(state='disabled', bg='LIGHTGREY')

            self.va.config(state='disabled', bg='LIGHTGREY')
            self.vpw.config(state='disabled', bg='LIGHTGREY')
            self.vs.config(state='disabled', bg='LIGHTGREY')

            self.aa.config(state='disabled', bg='LIGHTGREY')
            self.apw.config(state='disabled', bg='LIGHTGREY')
            self.ase.config(state='disabled', bg='LIGHTGREY')

            self.msr.config(state='disabled', bg='LIGHTGREY')
            self.at.config(state='disabled', bg='LIGHTGREY')
            self.ret.config(state='disabled', bg='LIGHTGREY')
            self.rf.config(state='disabled', bg='LIGHTGREY')
            self.rt.config(state='disabled', bg='LIGHTGREY')
            
        # if the mode is not off - allow user to set pulse rate
        else:
            self.lpr.config(state='normal', bg='WHITE')
            self.upr.config(state='normal', bg='WHITE')

        # if the mode has rate modulation - allow user to set maximum sensor rate, activity threshold, reaction time, response time, and recovery time,
        # otherwise do not    
        if mode in {'AOOR','AAIR','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR'}:
            self.msr.config(state='normal', bg='WHITE')
            self.at.config(state='normal', bg='WHITE')
            self.ret.config(state='normal', bg='WHITE')
            self.rf.config(state='normal', bg='WHITE')
            self.rt.config(state='normal', bg='WHITE')
        else:
            self.msr.config(state='disabled', bg='LIGHTGREY')
            self.at.config(state='disabled', bg='LIGHTGREY')
            self.ret.config(state='disabled', bg='LIGHTGREY')
            self.rf.config(state='disabled', bg='LIGHTGREY')
            self.rt.config(state='disabled', bg='LIGHTGREY')

        # if the mode has dual sensing - all the user to set fixed av delay, otherwise do not
        if mode in {'VDD','DOO','DDI','DDD','VDDR','DOOR','DDIR','DDDR'}:
            self.favd.config(state='normal', bg='WHITE')
            
            # of the modes with dual sensing, if the mode has dual tracked sensing - allow user to set atr duration, atr fallback mode,
            # atr fallback time, pvarp extension, and dynamic av delay,otherwise do not
            if mode in {'VDD','DDD','VDDR','DDDR'}:
                self.atrfm.config(state='normal')
                self.davd.config(state='normal')
                self.pvarpeOn.config(state='normal')
            
                # of the modes with dual tracked sensing, if the mode is dual chamber - allow user to set sensed av delay offset, otherwise do not
                if mode in {'DDD','DDDR'}:
                    self.savdoOn.config(state='normal')
                else:
                    self.savdoOn.deselect()
                    self.__enable_savdo()
                    self.savdoOn.config(state='disabled')
                
            else:
                self.atrfm.deselect()
                self.__enable_atr()
                self.atrfm.config(state='disabled')
                self.davd.config(state='disabled')
                self.savdoOn.deselect()
                self.__enable_savdo()
                self.savdoOn.config(state='disabled')
                self.pvarpeOn.deselect()
                self.__enable_pvarpe()
                self.pvarpeOn.config(state='disabled')

        else:
            self.atrfm.deselect()
            self.__enable_atr()
            self.atrfm.config(state='disabled')
            self.davd.config(state='disabled')
            self.savdoOn.deselect()
            self.__enable_savdo()
            self.savdoOn.config(state='disabled')
            self.favd.config(state='disabled', bg='LIGHTGREY')
            self.pvarpeOn.deselect()
            self.__enable_pvarpe()
            self.pvarpeOn.config(state='disabled')
            
        # if mode involves atrial pacing - allow user to set atrial amplitude and atrial pace width, otherwise do not
        if mode in {'AAT','AOO','AAI','DOO','DDI','DDD','AOOR','AAIR','DOOR','DDIR','DDDR'}:
            self.aa.config(state='normal', bg='WHITE')
            self.apw.config(state='normal', bg='WHITE')

            # if mode involves sensing of the atrial chamber - allow the user to set atrial sensitivity, atrial refractory period, and post ventricular
            # atrial refractory period, otherwise do not
            if mode in {'AAT','AAI','DDI','DDD','AAIR','DDIR','DDDR'}:
                self.ase.config(state='normal', bg='WHITE')
                self.arp.config(state='normal', bg='WHITE')
                self.pvarp.config(state='normal', bg='WHITE')
            else:
                self.ase.config(state='disabled', bg='LIGHTGREY')
                self.arp.config(state='disabled', bg='LIGHTGREY')
                self.pvarp.config(state='disabled', bg='LIGHTGREY')
        else:
            self.aa.config(state='disabled', bg='LIGHTGREY')
            self.apw.config(state='disabled', bg='LIGHTGREY')
            self.ase.config(state='disabled', bg='LIGHTGREY')
            self.arp.config(state='disabled', bg='LIGHTGREY')
            self.pvarp.config(state='disabled', bg='LIGHTGREY')

        # if mode involves ventricular pacing - allow the user to set venricular amplitude and ventricular pace width, otherwise do not
        if mode in {'VVT','VOO','VVI','VDD','DOO','DDI','DDD','VOOR','VVIR','VDDR','DOOR','DDIR','DDDR'}:
            self.va.config(state='normal', bg='WHITE')
            self.vpw.config(state='normal', bg='WHITE')

            #if mode involves ventricular sensing - allow the user to set ventricular sensitivity and ventricular refractory period, otherwise do not
            if mode in {'VVT','VVI','VDD','DDI','DDD','VVIR','VDDR','DDIR','DDDR'}:
                self.vs.config(state='normal', bg='WHITE')
                self.vrp.config(state='normal', bg='WHITE')
            else:
                self.vs.config(state='disabled', bg='LIGHTGREY')
                self.vrp.config(state='disabled', bg='LIGHTGREY')
        else:
            self.va.config(state='disabled', bg='LIGHTGREY')
            self.vpw.config(state='disabled', bg='LIGHTGREY')
            self.vs.config(state='disabled', bg='LIGHTGREY')
            self.vrp.config(state='disabled', bg='LIGHTGREY')

        # if mode falls into list below - allow the user to set rate smoothing, otherwise do not
        if mode in {'AAI','VVI','AAIR','VVIR','DDD','DDDR','VDD','VDDR'}:
            self.rsOn.config(state='normal')

            # if mode falls into list below - allow the user to set hysterisis, otherwise do not
            if mode in {'AAI','VVI','AAIR','VVIR','DDD','DDDR'}:
                self.hOn.config(state='normal')
            else:
                self.hOn.deselect()
                self.__enable_hys()
                self.hOn.config(state='disabled')
        else:
            self.rsOn.deselect()
            self.__enable_rs()
            self.rsOn.config(state='disabled')
            self.hOn.deselect()
            self.__enable_hys()
            self.hOn.config(state='disabled')

    def __change_state(self,state):
        if state == 'Permanent':
            self.modeMenu.config(state='normal', bg='WHITE')
        else:
            self.__change_mode('OFF')
            self.mode.set('OFF')
            self.modeMenu.config(state='disabled', bg='LIGHTGREY')
            
        #### Will need to incorporate additional states if necessary (at the moment, only 'Permanent' is enabled

        
    # Method to send (print at the moment) the set parameters    
    def __send_param(self):

        if (int(self.upperPulseRate.get()) < int(self.lowerPulseRate.get())):
            Popup("Parameter Error", "Lower Pulse Rate Limit must be less than Upper Pulse Rate Limit")
        else:
            Popup("Parameter Transmission","Parameters are being transmitted to the Pacemaker")
            print(self.mode.get())
        
            if self.mode.get() == "VOO":
                print("Upper Pulse Rate Limit: " + self.upperPulseRate.get() + "ppm")
                print("Lower Pulse Rate Limit: " + self.lowerPulseRate.get() + "ppm")
                print("Ventricular Amplitude: " + self.vAmp.get() + "V")
                print("Ventricular Pulse Width: " + self.vPulseWidth.get() + "mV")

            
        #### Will need to use serial communication to send parameters to the board
        #### Will need to write code which will send all parameters for each new mode to the board;
        ####  at the moment VOO mode only

    # Method to request more info on the parameters
    def __more_info(self):
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
    def __start_egram(self):
        self.egramWindow = Toplevel(self.master)
        self.loginWindow = Egram_Window(self.egramWindow)

    def __enable_hys(self):
        if self.hysOn.get():
            self.h.config(state='normal', bg='WHITE')
        else:
            self.h.config(state='disabled', bg='LIGHTGREY')

    def __enable_atr(self):
        if self.atrOn.get():
            self.atrd.config(state='normal', bg='WHITE')
            self.atrft.config(state='normal', bg='WHITE')
        else:
            self.atrft.config(state='disabled', bg='LIGHTGREY')
            self.atrd.config(state='disabled', bg='LIGHTGREY')

    def __enable_rs(self):
        if self.rateSmoothOn.get():
            self.rs.config(state='normal', bg='WHITE')
        else:
            self.rs.config(state='disabled', bg='LIGHTGREY')

    def __enable_savdo(self):
        if self.savdOffsetOn.get():
            self.savdo.config(state='normal', bg='WHITE')
        else:
            self.savdo.config(state='disabled', bg='LIGHTGREY')

    def __enable_pvarpe(self):
        if self.postVARPExtOn.get():
            self.pvarpe.config(state='normal', bg='WHITE')
        else:
            self.pvarpe.config(state='disabled', bg='LIGHTGREY')