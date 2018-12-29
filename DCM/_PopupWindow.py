import tkinter
from tkinter import *

#************************ POPUP WINDOW DEFINITION ***************************

def Popup(popup_title,popup_description):
    win = Toplevel()
    win.wm_title(popup_title)

    Label(win, text=popup_description).grid(row=2, column=0)
    Button(win, text="Okay", command=win.destroy).grid(row=3, column=0)