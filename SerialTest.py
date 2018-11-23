from _SerialHandler import *
from serial import *
import struct
import time

#Always keep this line in - adjust to your COM port
<<<<<<< HEAD
port = SerialHandler("COM13")

#Comment this line if you are sending Data
#port.startSerialListen(4, 'hh', print) # f = float, h = int16, 4 = # of bytes

#Comment these lines if you are receiving Data
#port.sendData([22,4])
#time.sleep(2)
#port.sendData([22,4])


#port = Serial("COM13", 9600, stopbits=STOPBITS_ONE)
port.startSerialListen(8, 'ff', print)
time.sleep(2)
port.stopSerialListen()
# for i in range(20):
#     if (port.in_waiting % 4 == 0 and port.in_waiting > 0):
#        print(port.in_waiting)
#        dat = port.read(port.in_waiting)
#        print(dat)
#        #output = struct.unpack('hh', dat)
#        #print(output)

# for i in range(20):
#     print(port.in_waiting)
#     dat = port.read(4)
#     print(dat)
#     #time.sleep(0.5)
#     if(port.in_waiting == 4096):
#         port.reset_input_buffer()
#
# port.close()
=======
port = SerialHandler("COM3")

#Comment this line if you are sending Data
port.startSerialListen(4, 'hh', print) # f = float, h = int16, 4 = # of bytes

#Comment these lines if you are receiving Data
#port.sendData([22, 42])
#time.sleep(2)
#port.sendData([22, 41])

>>>>>>> 5b0fd37567a56842fbfbaa534d5410da5775a84e
