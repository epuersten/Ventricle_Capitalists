# when the window is exited, print the patients parameters to a file with the name of the patient
# when the window is entered, read from the patients file to set each of the parameters

import csv
import tkinter
from tkinter import *
from _LoginWindow import *
from _EgramWindow import *
from _SerialHandler import *

#Home Window.

class Home_Window(Frame):
    def __init__(self,master,username):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor 2.0 Home")
        master.config(background='white')

        self.filename = str(username) + ".txt"

        self.current_params = []
        self.new_params = []

        self.port = SerialHandler("COM3") #Serial Port to use

        Label(master, text="Parameter Selection", bg = 'white', font = 12).grid(row=1, column=1)

        select_frame = Frame(master, bg = 'white')
        select_frame.grid(row = 2, column = 1)

        button_frame = Frame(master, bg = 'white')
        button_frame.grid(row = 3, column = 1)

        param_frame = Frame(select_frame, bg = 'gray92')
        param_frame.grid(row = 2, column = 1, padx = 20, pady = 20)
        
        ms_frame = Frame(select_frame, bg = 'white')
        ms_frame.grid(row = 1, column = 1)

        pr_frame = Frame(param_frame, bg = 'gray92', padx=30, pady=30)
        pr_frame.grid(row = 1, column = 1)

        vent_frame = Frame(param_frame, bg = 'gray92', padx=30, pady=30)
        vent_frame.grid(row = 1, column = 2)

        atrial_frame = Frame(param_frame, bg = 'gray92', padx=30, pady=30)
        atrial_frame.grid(row = 1, column = 3)

        atr_frame = Frame(param_frame, bg = 'gray92', padx=30, pady=30)
        atr_frame.grid(row = 1, column = 4)

        delay_frame = Frame(param_frame, bg = 'gray92', padx=30)
        delay_frame.grid(row = 2, column = 1)
        
        rsh_frame = Frame(param_frame, bg = 'gray92', padx=30)
        rsh_frame.grid(row = 2, column = 2)

        rp_frame = Frame(param_frame, bg = 'gray92', padx=30)
        rp_frame.grid(row = 2, column = 3)

        misc_frame = Frame(param_frame, bg = 'gray92', padx=30)
        misc_frame.grid(row = 2, column = 4)

        # Create buttons to Send Parameters, Change Patients, get More Information, Start/Stop Egram Transmission
        Button(button_frame, text="Information", command=self.__more_info, bg = 'royal blue', fg = 'white').grid(row=1, column=1, padx=10, pady=10)
        Button(button_frame, text="Electrogram Viewer", command=self.__start_egram, bg = 'royal blue', fg = 'white').grid(row=1, column=2, padx=10, pady=10)
        Button(button_frame, text="Send Parameters", command=self.__send_param, bg = 'royal blue', fg = 'white').grid(row=1, column=3, padx=10, pady=10)
        Button(button_frame, text="Change Patients", command=self.__exit, bg = 'royal blue', fg = 'white').grid(row=1, column=4, padx=10, pady=10)
        Button(button_frame, text="QUIT", command = self.__exit, bg = 'red', fg = 'white').grid(row=1,column=5, padx = 10, pady = 10)

        # Create Mode Selection
        
        Label(ms_frame, text="Select a Mode", bg = 'white').grid(row = 1, column = 1, pady=3, sticky=E)
        
        modes = [ 'OFF','VOO','AOO','VVI','AAI','DOO','DDD','VOOR','AOOR','VVIR','AAIR','DOOR','DDDR']
        # VVT, AAT, VDD, DDI, , DDIR and VDDR were removed as these modes are not part of any assignment
        self.mode = StringVar(master)
        self.mode.set(modes[0]) 

        self.modeMenu = OptionMenu(ms_frame, self.mode, *modes, command = self.__change_mode)
        self.modeMenu.config(bg = 'white')
        self.modeMenu.grid(row = 1, column = 2, pady=3, sticky=W)

        # Create State Selection

        Label(ms_frame, text="Select a State", bg = 'white').grid(row = 1, column = 3, pady=3, sticky=E)
        
        states = ['Permanent','Temporary','Pace-Now','Magnet','Power-On Reset']
        self.state = StringVar(master)
        self.state.set(states[0]) 
 
        self.stateMenu = OptionMenu(ms_frame, self.state, *states, command = self.__change_state)
        self.stateMenu.config(bg = 'white')
        self.stateMenu.grid(row = 1, column = 4, pady=3, sticky=W)

        # Create label and variable entry field for Pace Rate Parameter

        Label(pr_frame, text="Upper Pace Rate (ppm)", bg = 'gray92').grid(row=5, column=2, sticky=E, pady=3)
        uprates = list(range(50,176,5))
        self.upperPulseRate = StringVar()
        self.upperPulseRate.set('120') 
        self.upr = OptionMenu(pr_frame, self.upperPulseRate, *uprates)
        self.upr.config(state='disabled', bg='LIGHTGRAY')
        self.upr.grid(row = 5, column = 3, pady=3, sticky=W)

        Label(pr_frame, text="Lower Pace Rate (ppm)", bg = 'gray92').grid(row=6, column=2, sticky=E, pady=3)
        lprates = list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        self.lowerPulseRate = StringVar()
        self.lowerPulseRate.set('60') 
        self.lpr = OptionMenu(pr_frame, self.lowerPulseRate, *lprates)
        self.lpr.config(state='disabled', bg='LIGHTGRAY')
        self.lpr.grid(row = 6, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for ventricular parameters
        Label(vent_frame, text="Ventricular Pulse Width (ms)", bg = 'gray92').grid(row=5, column=5, sticky=E)
        venpws = range(10,20)
        self.vPulseWidth = StringVar()
        self.vPulseWidth.set(10) 
        self.vpw = OptionMenu(vent_frame, self.vPulseWidth, *venpws)
        self.vpw.config(state='disabled', bg='LIGHTGREY')
        self.vpw.grid(row = 5, column = 6, pady=3, sticky=W)

        Label(vent_frame, text="Ventricular Amplitude (V)", bg = 'gray92').grid(row=6, column=5, sticky=E, pady=3)
        vas = ['0.00','1.25','2.50','3.75','5.00']
        self.vAmp = StringVar()
        self.vAmp.set(3.75) 
        self.va = OptionMenu(vent_frame, self.vAmp, *vas)
        self.va.config(state='disabled', bg='LIGHTGREY')
        self.va.grid(row = 6, column = 6, pady=3, sticky=W)

        Label(vent_frame, text="Ventricular Sensitivity (mV)", bg = 'gray92').grid(row=7, column=5, sticky=E)
        vsens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.vSensitivity = StringVar()
        self.vSensitivity.set(2.5) 
        self.vs = OptionMenu(vent_frame, self.vSensitivity, *vsens)
        self.vs.config(state='disabled', bg='LIGHTGREY')
        self.vs.grid(row = 7, column = 6, pady=3, sticky=W)

        # Create labels and variable entry fields for atrial parameters
        Label(atrial_frame, text="Atrial Pulse Width (ms)", bg = 'gray92').grid(row=5, column=8, sticky=E, pady=3)
        atrpws = range(10,20)
        self.aPulseWidth = StringVar()
        self.aPulseWidth.set(10) 
        self.apw = OptionMenu(atrial_frame, self.aPulseWidth, *atrpws)
        self.apw.config(state='disabled', bg='LIGHTGREY')
        self.apw.grid(row = 5, column = 9, pady=3, sticky=W)

        Label(atrial_frame, text="Atrial Amplitude (V)", bg = 'gray92').grid(row=6, column=8, sticky=E)
        aas = ['0.00','1.25','2.50','3.75','5.00']
        self.aAmp = StringVar()
        self.aAmp.set(3.75) 
        self.aa = OptionMenu(atrial_frame, self.aAmp, *aas)
        self.aa.config(state='disabled', bg='LIGHTGREY')
        self.aa.grid(row = 6, column = 9, pady=3, sticky=W)

        Label(atrial_frame, text="Atrial Sensitivity (mV)", bg = 'gray92').grid(row=7, column=8, sticky=E)
        asens = ['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0']
        self.aSensitivity = StringVar()
        self.aSensitivity.set(0.75) 
        self.ase = OptionMenu(atrial_frame, self.aSensitivity, *asens)
        self.ase.config(state='disabled', bg='LIGHTGREY')
        self.ase.grid(row = 7, column = 9, pady=3, sticky=W)

        # Create labels and entry fields for ATR parameters
        self.atrOn = IntVar()
        self.atrfm = Checkbutton(atr_frame, text="ATR Fallback Mode", bg = 'gray92', variable=self.atrOn, state='disabled', command = self.__enable_atr)
        self.atrfm.grid(row=9, column=2, sticky=W)

        Label(atr_frame, text="ATR Duration (cc)", bg = 'gray92').grid(row=10, column=2, sticky=E)
        atrdurs = [10] + list(range(20,81,20)) + list(range(100, 2001,100))
        self.atrDuration = StringVar()
        self.atrDuration.set('20') 
        self.atrd = OptionMenu(atr_frame, self.atrDuration, *atrdurs)
        self.atrd.config(state='disabled', bg='LIGHTGREY')
        self.atrd.grid(row = 10, column = 3, pady=3, sticky=W)

        Label(atr_frame, text="ATR Fallback Time (min)", bg = 'gray92').grid(row=11, column=2, sticky=E)
        ftimes = range(1,6)
        self.atrFallbackTime = StringVar()
        self.atrFallbackTime.set('1') 
        self.atrft = OptionMenu(atr_frame, self.atrFallbackTime, *ftimes)
        self.atrft.config(state='disabled', bg='LIGHTGREY')
        self.atrft.grid(row = 11, column = 3, pady=3, sticky=W)

        # Create labels and variable entry fields for Rate Smoothing and Hysteresis
        self.rateSmoothOn = IntVar()
        self.rsOn = Checkbutton(rsh_frame, text="Rate Smoothing", bg = 'gray92', variable=self.rateSmoothOn, state='disabled', command = self.__enable_rs)
        self.rsOn.grid(row=9, column=5, sticky=W)

        Label(rsh_frame, text="Rate Smoothing (%)", bg = 'gray92').grid(row=10, column=5, sticky=E)
        rsmooths = list(range(3,24,3)) + [25]
        self.rateSmoothing = StringVar()
        self.rateSmoothing.set('3') 
        self.rs = OptionMenu(rsh_frame, self.rateSmoothing, *rsmooths)
        self.rs.config(state='disabled', bg='LIGHTGREY')
        self.rs.grid(row = 10, column = 6, pady=6, sticky=W)

        self.hysOn = IntVar()
        self.hOn = Checkbutton(rsh_frame, text="Hysteresis", bg = 'gray92', variable=self.hysOn, state='disabled', command = self.__enable_hys)
        self.hOn.grid(row=11, column=5, sticky=W)

        Label(rsh_frame, text="Hysteresis Rate (ppm)", bg = 'gray92').grid(row=12, column=5, sticky=E)
        hysrates = list(range(30,50,5)) + list(range(50,90,1)) + list(range(90,176,5))
        self.hys = StringVar()
        self.hys.set('60') 
        self.h = OptionMenu(rsh_frame, self.hys, *hysrates)
        self.h.config(state='disabled', bg='LIGHTGREY')
        self.h.grid(row = 12, column = 6, pady=6, sticky=W)

        # Create labels and variable entry fields for refractory period parameters
        Label(rp_frame, text="VRP (ms)", bg = 'gray92').grid(row=9, column=8, sticky=E)
        vrpvars = range(150,501,10)
        self.vRefractPeriod = StringVar()
        self.vRefractPeriod.set(320) 
        self.vrp = OptionMenu(rp_frame, self.vRefractPeriod, *vrpvars)
        self.vrp.config(state='disabled', bg='LIGHTGREY')
        self.vrp.grid(row = 9, column = 9, pady=3, sticky=W)
        
        Label(rp_frame, text="ARP (ms)", bg = 'gray92').grid(row=10, column=8, sticky=E)
        arpvars = range(150,501,10)
        self.aRefractPeriod = StringVar()
        self.aRefractPeriod.set(250) 
        self.arp = OptionMenu(rp_frame, self.aRefractPeriod, *arpvars)
        self.arp.config(state='disabled', bg='LIGHTGREY')
        self.arp.grid(row = 10, column = 9, pady=3, sticky=W)

        Label(rp_frame, text="PVARP (ms)", bg = 'gray92').grid(row=11, column=8, sticky=E)
        pvarpvars = range(150,501,10)
        self.postVARefractPeriod = StringVar()
        self.postVARefractPeriod.set(250) 
        self.pvarp = OptionMenu(rp_frame, self.postVARefractPeriod, *pvarpvars)
        self.pvarp.config(state='disabled', bg='LIGHTGREY')
        self.pvarp.grid(row = 11, column = 9, pady=3, sticky=W)

        self.postVARPExtOn = IntVar()
        self.pvarpeOn = Checkbutton(rp_frame, text="PVARP Extension", bg = 'gray92', variable=self.postVARPExtOn, state='disabled', command = self.__enable_pvarpe)
        self.pvarpeOn.grid(row=12, column=8, sticky=W)

        Label(rp_frame, text="PVARP Extension (ms)", bg = 'gray92').grid(row=13, column=8, sticky=E)
        pvarpevars = range(50,401,50)
        self.postVARefractPeriodExt = StringVar()
        self.postVARefractPeriodExt.set('50') 
        self.pvarpe = OptionMenu(rp_frame, self.postVARefractPeriodExt, *pvarpevars)
        self.pvarpe.config(state='disabled', bg='LIGHTGREY')
        self.pvarpe.grid(row = 13, column = 9, pady=3, sticky=W)
        
        # Create labels and variable entry fields for AV Delay Parameters
        self.dynAVDelayOn = IntVar()
        self.davdOn = Checkbutton(delay_frame, text="Dynamic AV Delay", bg = 'gray92', variable=self.dynAVDelayOn, state='disabled', command = self.__enable_davd)
        self.davdOn.grid(row=14, column=5, sticky=W)

        Label(delay_frame, text="Minimum Dynamic AV Delay (ms)", bg = 'gray92').grid(row=15, column=5, sticky=E)
        davdelays = range(70,301,10)
        self.dynAVDelay = StringVar()
        self.dynAVDelay.set('150') 
        self.davd = OptionMenu(delay_frame, self.dynAVDelay, *davdelays)
        self.davd.config(state='disabled', bg='LIGHTGREY')
        self.davd.grid(row =15, column = 6, pady=3, sticky=W)
        
        Label(delay_frame, text="Fixed AV Delay (ms)", bg = 'gray92').grid(row=16, column=5, sticky=E)
        favdelays = range(70,301,10)
        self.fixedAVDelay = StringVar()
        self.fixedAVDelay.set('150') 
        self.favd = OptionMenu(delay_frame, self.fixedAVDelay, *favdelays)
        self.favd.config(state='disabled', bg='LIGHTGREY')
        self.favd.grid(row =16, column = 6, pady=3, sticky=W)

        self.savdOffsetOn = IntVar()
        self.savdoOn = Checkbutton(delay_frame, text="Sensed AV Delay Offset", bg = 'gray92', variable=self.savdOffsetOn, state='disabled', command = self.__enable_savdo)
        self.savdoOn.grid(row=17, column=5, sticky=W)

        Label(delay_frame, text="Sensed AV Delay Offset (ms)", bg = 'gray92').grid(row=18, column=5, sticky=E)
        savdoffsets = list(range(-10,-101,-10))
        self.sensedAVDelayOffset = StringVar()
        self.sensedAVDelayOffset.set('-10') 
        self.savdo = OptionMenu(delay_frame, self.sensedAVDelayOffset, *savdoffsets)
        self.savdo.config(state='disabled', bg='LIGHTGREY')
        self.savdo.grid(row = 18, column = 6, pady=3, sticky=W)

        # Create labels and variable entry fields for Maximum Sensor Rate, Activity Threshold, Reaction Time, Response Factor, and Recovery Time        
        Label(misc_frame, text="Activity Threshold", bg = 'gray92').grid(row=13, column=2, sticky=E)
        thresholds = [ 'V-Low','Low','Med-Low','Med','Med-High','High','V-High']
        self.activityThreshold = StringVar()
        self.activityThreshold.set('Med') 
        self.at = OptionMenu(misc_frame, self.activityThreshold, *thresholds)
        self.at.config(state='disabled', bg='LIGHTGREY')
        self.at.grid(row = 13, column = 3, pady=3, sticky=W)
        
        Label(misc_frame, text="Reaction Time (sec)", bg = 'gray92').grid(row=14, column=2, sticky=E)
        rtimes = range(10,51,10)
        self.reactionTime = StringVar()
        self.reactionTime.set('30') 
        self.ret = OptionMenu(misc_frame, self.reactionTime, *rtimes)
        self.ret.config(state='disabled', bg='LIGHTGREY')
        self.ret.grid(row = 14, column = 3, pady=3, sticky=W)

        Label(misc_frame, text="Response Factor", bg = 'gray92').grid(row=15, column=2, sticky=E)
        rfactors = range(1,17)
        self.responseFactor = StringVar()
        self.responseFactor.set('8') 
        self.rf = OptionMenu(misc_frame, self.responseFactor, *rfactors)
        self.rf.config(state='disabled', bg='LIGHTGREY')
        self.rf.grid(row = 15, column = 3, pady=3, sticky=W)

        Label(misc_frame, text="Recovery Time (min)", bg = 'gray92').grid(row=16, column=2, sticky=E)
        rtimes = range(2,17)
        self.recoveryTime = StringVar()
        self.recoveryTime.set('5') 
        self.rt = OptionMenu(misc_frame, self.recoveryTime, *rtimes)
        self.rt.config(state='disabled', bg='LIGHTGREY')
        self.rt.grid(row = 16, column = 3, pady=3, sticky=W)

        Label(misc_frame, text="Maximum Sensor Rate (ppm)", bg = 'gray92').grid(row=17, column=2, sticky=E)
        msrates = range(50,176,5)
        self.maxSensorRate = StringVar()
        self.maxSensorRate.set('120') 
        self.msr = OptionMenu(misc_frame, self.maxSensorRate, *msrates)
        self.msr.config(state='disabled', bg='LIGHTGREY')
        self.msr.grid(row = 17, column = 3, pady=3, sticky=W)
            
        # call to retrieve user parameters
        self.__retrieve_params()

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

            self.davdOn.deselect()
            self.__enable_davd()
            self.davdOn.config(state='disabled')
            
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
                self.davdOn.config(state='normal')
                self.__enable_davd()
                self.pvarpeOn.config(state='normal')
            
                # of the modes with dual tracked sensing, if the mode is dual chamber - allow user to set sensed av delay offset, otherwise do not
                if mode in {'DDD','DDDR'}:
                    self.savdoOn.config(state='normal')
                else:
                    self.savdoOn.deselect()
                    self.savdoOn.config(state='disabled')
                
            else:
                self.atrfm.deselect()
                self.__enable_atr()
                self.atrfm.config(state='disabled')

                self.davdOn.deselect()
                self.__enable_davd()
                self.davdOn.config(state='disabled')
            
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

            self.davdOn.deselect()
            self.__enable_davd()
            self.davdOn.config(state='disabled')

            
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

        
    # Method to send the set parameters    
    def __send_param(self):
        
        if self.__check_param(self.current_params):
            Popup("Error", "Parameters were not changed and cannot be transmitted")
        
        else:
            self.current_params = self.new_params
            if (int(self.upperPulseRate.get()) < int(self.lowerPulseRate.get())):
                Popup("Parameter Error", "Lower Pulse Rate Limit must be less than Upper Pulse Rate Limit")
            else:
                modeEnumeration = self.__encode_mode(self.current_params)
                actThreshEnumeration = self.__encode_actThresh(self.current_params)
                self.current_params[0] = modeEnumeration
                self.current_params[27] = actThreshEnumeration
                Popup("Parameter Transmission","Parameters are being transmitted to the Pacemaker")
                print(self.current_params)
                self.port.sendData(self.current_params)
                #Echo Code - for testing
                #h = int16 (2 bytes), f = floating point (4 bytes)
                #self.port.startSerialListen(26, "hhhhhhhhhff")


    def __encode_mode(self,current_params):
        modeEnum = ['OFF','VOO','AOO','VVI','AAI','DOO','DDD','VOOR','AOOR','VVIR','AAIR','DOOR','DDDR']
        for i in range(len(modeEnum)):
            if current_params[0] == modeEnum[i]:
                    mode = i
        return mode

    def __encode_actThresh(self,current_params):
        actThreshEnum = ['V-Low','Low','Med-Low','Med','Med-High','High','V-High']
        for i in range(len(actThreshEnum)):
            if current_params[27] == actThreshEnum[i]:
                    actThresh = i+1
        return actThresh
                    
    # Method to check if the parameters have changed since the last time they were sent
    def __check_param(self,current_params):
        self.new_params = [self.mode.get(), self.lowerPulseRate.get(), self.upperPulseRate.get(), self.maxSensorRate.get(), self.fixedAVDelay.get(), self.dynAVDelayOn.get(), self.dynAVDelay.get(), self.savdOffsetOn.get(), self.sensedAVDelayOffset.get(), self.vAmp.get(), self.aAmp.get(), self.vPulseWidth.get(), self.aPulseWidth.get(), self.vSensitivity.get(), self.aSensitivity.get(), self.vRefractPeriod.get(),self.aRefractPeriod.get(), self.postVARefractPeriod.get(),self.postVARPExtOn.get(),self.postVARefractPeriodExt.get(), self.hysOn.get(), self.hys.get(),self.rateSmoothOn.get(), self.rateSmoothing.get(), self.atrOn.get(), self.atrDuration.get(), self.atrFallbackTime.get(),self.activityThreshold.get(),self.reactionTime.get(),self.responseFactor.get(),self.recoveryTime.get()]
        if len(self.new_params) != len(self.current_params):
            return(0)
        else:
            for i in range(len(self.new_params)):
                if self.new_params[i] != self.current_params[i]:
                    return(0)
            return(1)

    # Method to request more info on the parameters
    def __more_info(self):
        win = Toplevel()
        win.wm_title("About Mode and State Selection")
        win.config(bg = 'white')

        Label(win,bg='white', text = 'Mode and State Selection').grid(row=1, column =1)
        
        Label(win, bg='white', justify = LEFT, text = """Start by selecting a mode and a state
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

            Depending on the mode selected different parameters will become available to set""").grid(row = 2, column = 1)

        Button(win, text="Okay", command=win.destroy).grid(row=3, column=1)


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

    def __enable_davd(self):
        if self.dynAVDelayOn.get():
            self.davd.config(state='normal', bg='WHITE')
        else:
            self.davd.config(state='disabled', bg='LIGHTGREY')

    def __retrieve_params(self):
        try:
            userFile = open(self.filename,"r")
            sourceData = csv.DictReader(userFile, fieldnames=['parameter'])
        
            # this needs to be swapped out to transfer all the saved parameters
            index = 0

            for row in sourceData:
                if index == 0:
                    self.mode.set(row['parameter'])
                    self.__change_mode(self.mode.get())
                elif index == 1:
                    self.lowerPulseRate.set(row['parameter'])
                elif index == 2:
                    self.upperPulseRate.set(row['parameter'])
                elif index == 3:
                    self.maxSensorRate.set(row['parameter'])
                elif index == 4:
                    self.fixedAVDelay.set(row['parameter'])
                elif index == 5:
                    self.dynAVDelayOn.set(row['parameter'])
                elif index == 6:
                    self.dynAVDelay.set(row['parameter'])
                elif index == 7:
                    self.savdOffsetOn.set(row['parameter'])
                elif index == 8:
                    self.sensedAVDelayOffset.set(row['parameter'])
                elif index == 9:
                    self.vAmp.set(row['parameter'])
                elif index == 10:
                    self.aAmp.set(row['parameter'])
                elif index == 11:
                    self.vPulseWidth.set(row['parameter'])
                elif index == 12:
                    self.aPulseWidth.set(row['parameter'])
                elif index == 13:
                    self.vSensitivity.set(row['parameter'])
                elif index == 14:
                    self.aSensitivity.set(row['parameter'])
                elif index == 15:
                      self.vRefractPeriod.set(row['parameter'])
                elif index == 16:
                      self.aRefractPeriod.set(row['parameter'])
                elif index == 17:
                      self.postVARefractPeriod.set(row['parameter'])
                elif index == 18:
                      self.postVARPExtOn.set(row['parameter'])
                elif index == 19:
                      self.postVARefractPeriodExt.set(row['parameter'])
                elif index == 20:
                      self.hysOn.set(row['parameter'])
                elif index == 21:
                      self.hys.set(row['parameter'])
                elif index == 22:
                      self.rateSmoothOn.set(row['parameter'])
                elif index == 23:
                      self.rateSmoothing.set(row['parameter'])
                elif index == 24:
                      self.atrOn.set(row['parameter'])
                elif index == 25:
                      self.atrDuration.set(row['parameter'])
                elif index == 26:         
                      self.atrFallbackTime.set(row['parameter'])
                elif index == 27:
                      self.activityThreshold.set(row['parameter'])
                elif index == 28:
                      self.reactionTime.set(row['parameter'])
                elif index == 29:
                      self.responseFactor.set(row['parameter'])
                elif index == 30:
                      self.recoveryTime.set(row['parameter'])
                index=index + 1

            self.__enable_hys()
            self.__enable_atr()
            self.__enable_rs()
            self.__enable_savdo()
            self.__enable_pvarpe()
            self.__enable_davd()

            
        except: #If file does not exist, create it
            userFile = open(self.filename, "w")

        userFile.close()
        

    # on termination of the window the parameters are saved in a file with the same name as the user's username
    def __exit(self):

        userFile = open(self.filename, "w")
        userFile.close()
        userFile = open(self.filename, "a+")
        sourceWriter = csv.DictWriter(userFile, fieldnames=['parameter'])

        self.new_params = [self.mode.get(), self.lowerPulseRate.get(), self.upperPulseRate.get(), self.maxSensorRate.get(), self.fixedAVDelay.get(), self.dynAVDelayOn.get(), self.dynAVDelay.get(), self.savdOffsetOn.get(), self.sensedAVDelayOffset.get(), self.vAmp.get(), self.aAmp.get(), self.vPulseWidth.get(), self.aPulseWidth.get(), self.vSensitivity.get(), self.aSensitivity.get(), self.vRefractPeriod.get(),self.aRefractPeriod.get(), self.postVARefractPeriod.get(),self.postVARPExtOn.get(),self.postVARefractPeriodExt.get(), self.hysOn.get(), self.hys.get(),self.rateSmoothOn.get(), self.rateSmoothing.get(), self.atrOn.get(), self.atrDuration.get(), self.atrFallbackTime.get(),self.activityThreshold.get(),self.reactionTime.get(),self.responseFactor.get(),self.recoveryTime.get()]
        for i in range(len(self.new_params)):
            sourceWriter.writerow({'parameter' : str(self.new_params[i])})


        userFile.close()
        self.master.destroy()
            
    

                
              
