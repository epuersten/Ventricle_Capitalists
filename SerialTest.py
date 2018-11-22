from _SerialHandler import *
from serial import *
import struct

#port = SerialHandler("COM13")
#port.sendData([2])

port = Serial("COM13", 9600)
port.write(bytearray([2]))
