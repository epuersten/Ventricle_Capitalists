from _SerialHandler import *

port = SerialHandler("COM13")
port.sendData([10000])

