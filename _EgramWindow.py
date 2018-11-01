import tkinter
from tkinter import *
from _PopupWindow import *
from _HomeWindow import *

#Electrocardiogram Window

class Egram_Window(Frame):
    def __init__(self,master):
        
        self.master = master
        master.title("Pacemaker Device Control Monitor v 1.0 Electrogram Viewer")

        Label(master, text="Electrogram Here!").grid(row=1, column=1)

        Button(master, text="STOP EGRAM TRANSMISSION", command = master.destroy).grid(row=2,column=1)

        #### Will need to use serial communication to gather egram data from the board
        #### Will need to display egram data graphically
        #### Will need to use serial communication to halt egram data from the board