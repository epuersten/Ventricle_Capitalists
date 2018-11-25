import tkinter
from tkinter import *
from _PopupWindow import *
from _HomeWindow import *
from queue import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#********************** EGRAM WINDOW ****************************************

class Egram_Window(Frame):
    #ADDED NEW PARAMETER
    def __init__(self,master, port):
       
        self.liveFeed = False
        self.master = master
        master.title("Electrogram Viewer")
        
        master.config(background='white')
    
        Label(master, text="Electrogram Viewer", bg = 'white', font = 12).grid(row=1,column=1)

        graph_frame = Frame(master, bg = 'gray92', padx = 10, pady = 10)
        graph_frame.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        graph_fig = Figure()
        self.vent = graph_fig.add_subplot(311)
        self.atr = graph_fig.add_subplot(313)

        #ADDED THESE!!!!!!
        self.serPort = port #Serial port for input...
        self.serData = [0,0]
        
        self.__reset_feed()
        
        self.graph = FigureCanvasTkAgg(graph_fig, master=graph_frame)
        self.graph.get_tk_widget().grid(row=2,column=1)

        button_frame = Frame(master, bg = 'white', padx = 10, pady = 10)
        button_frame.grid(row = 3, column = 1)
        
        Button(button_frame, text="Start/Stop Feed", command=self.__update_feed, bg="royal blue", fg="white").grid(row=1,column=1, padx = 10, pady = 10)
        Button(button_frame, text="Clear Feed", command=self.__clear_feed, bg="royal blue", fg="white").grid(row = 1, column=2, padx = 10, pady = 10)
        Button(button_frame, text="Exit Viewer", command=master.destroy, bg="red", fg="white").grid(row=1,column=3, padx = 10, pady = 10)


        #ADDED THESE TO HOLD THE INPUT DATA
        self.vData = Queue(100) #Data queue with max size of 20 for storing ECG input. Ventricle sensor data
        self.aData = Queue(100) #Atrial sensor data

        #Fill the queue with empty data at first
        for i in range(100):
            self.vData.put(0)
            self.aData.put(0)


    def __update_feed(self):
        if self.liveFeed:
            self.liveFeed = False
            self.master.after_cancel(self.cont_id)
            self.serPort.stopSerialListen()
        else:
            self.liveFeed = True
            self.serPort.startSerialListen(8, 'ff', self.__serial_callback)
            self.__live_feed_serial()

    #Get live feed from the serial port
    def __live_feed_serial(self):

        if self.liveFeed:

            self.__reset_feed()
            self.vent.plot(range(100), self.vData.queue, marker=',', color='blue')
            self.atr.plot(range(100), self.aData.queue, marker=',', color='blue')
            self.graph.draw()

        self.cont_id = self.master.after(100, self.__live_feed_serial)




    #Callback function used by the serial thread to pass received data to local thingy
    #This is called everytime new data is received
    def __serial_callback(self, data):
        # Check serial data
        # If none, then we must have encountered an error
        if (data is None):
            self.liveFeed = False
            self.serPort.stopSerialListen()
            Popup("Telemetry Error", "Board Telemetry Lost!")
        else:
            self.vData.get()  # Pop oldest entry from the queue
            self.vData.put(data[0])  # Put in the new data

            self.aData.get()  # Ditto
            self.aData.put(data[1])




    def __clear_feed(self):

        self.liveFeed = False
        self.master.after_cancel(self.cont_id)
        self.__reset_feed()
        self.graph.draw()
        
    def __reset_feed(self):
        self.vent.cla()
        self.vent.grid()
        self.vent.set_ylim(top=5.0,bottom=-5.0)
        self.vent.set_xlim(right=99.0)
        self.vent.set_xlabel("Time (s)")
        self.vent.set_ylabel("Ventricular Amplitude (V)")
        
        self.atr.cla()
        self.atr.grid()
        self.atr.set_ylim(top=5.0,bottom=-5.0)
        self.atr.set_xlim(right=99.0)
        self.atr.set_xlabel("Time (s)")
        self.atr.set_ylabel("Atrial Amplitude (V)")
