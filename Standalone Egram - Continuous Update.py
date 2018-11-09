import csv

from tkinter import *
from random import randint
 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

#************************ POPUP WINDOW DEFINITION ***************************
def Popup(popup_title,popup_description):
    win = Toplevel()
    win.wm_title(popup_title)

    Label(win, text=popup_description).grid(row=2, column=0)
    Button(win, text="Okay", command=win.destroy).grid(row=3, column=0)

#*********************** STREAM OF DATA POINTS ******************************
 
def vent_data_points(x):
    f = open("vent_points.txt", "w")
    for i in range(x):
        f.write(str(randint(-5, 5))+'\n')
    f.close()
 
    f = open("vent_points.txt", "r")
    data = f.readlines()
    f.close()
 
    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l

def atr_data_points(x):
    f = open("atr_points.txt", "w")
    for i in range(x):
        f.write(str(randint(-5, 5))+'\n')
    f.close()
 
    f = open("atr_points.txt", "r")
    data = f.readlines()
    f.close()
 
    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l

#********************** EGRAM WINDOW ****************************************

class EgramWindow(Frame):
    def __init__(self,master):
       
        self.liveFeed = False
        
        self.master = master
        master.title("Electrogram Viewer")
        
        master.config(background='white')
    
        Label(root, text="Electrogram Viewer", bg = 'white', font = 12).grid(row=1,column=2)

        Button(root, text="Start/Stop Feed", command=self.__update_feed, bg="royal blue", fg="white").grid(row=3,column=2)
        Button(root, text="Exit Viewer", command=master.destroy, bg="red", fg="white").grid(row=5,column=3)
        Button(root, text="Clear Feed", command=self.__clear_feed, bg="royal blue", fg="white").grid(row = 4, column=2)
    
        fig = Figure()
    
        self.vent = fig.add_subplot(311)
        
        self.atr = fig.add_subplot(313)
        
        self.__reset_feed()
        
        self.graph = FigureCanvasTkAgg(fig, master=root)
        self.graph.get_tk_widget().grid(row=2,column=2)

    def __update_feed(self):
        if self.liveFeed:
            self.liveFeed = False
            root.after_cancel(self.cont_id)
        else:
            self.liveFeed = True
            self.__live_feed() 
            
    def __live_feed(self):

        if self.liveFeed:

            self.__reset_feed()
            
            dpts = vent_data_points(10)
            self.vent.plot(range(10), dpts, marker=',', color='blue')

            dpts = atr_data_points(10)
            self.atr.plot(range(10), dpts, marker=',', color='blue')

            self.graph.draw()

        self.cont_id = root.after(1000, self.__live_feed)

    def __clear_feed(self):

        self.liveFeed = False
        root.after_cancel(self.cont_id)
        self.__reset_feed()
        self.graph.draw()
        
    def __reset_feed(self):
        self.vent.cla()
        self.vent.grid()
        self.vent.set_ylim(top=5.0,bottom=-5.0)
        self.vent.set_xlim(right=9.0)
        self.vent.set_xlabel("Time (s)")
        self.vent.set_ylabel("Ventricular Amplitude (V)")
        
        self.atr.cla()
        self.atr.grid()
        self.atr.set_ylim(top=5.0,bottom=-5.0)
        self.atr.set_xlim(right=9.0)
        self.atr.set_xlabel("Time (s)")
        self.atr.set_ylabel("Atrial Amplitude (V)")
    
root = Tk()
egramWindow = EgramWindow(root)
root.mainloop()
