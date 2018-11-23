from _SerialHandler import *
from serial import *
import struct
import time

#Always keep this line in - adjust to your COM port
port = SerialHandler("COM3")

#Comment this line if you are sending Data
port.startSerialListen(4, 'hh', print) # f = float, h = int16, 4 = # of bytes

#Comment these lines if you are receiving Data
#port.sendData([22, 42])
#time.sleep(2)
#port.sendData([22, 41])

