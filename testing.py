from _SerialHandler import *
import time

handler = SerialHandler("COM3")

handler.sendData([1])
handler.sendData([2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8,8,8,8,88])

handler.startSerialListen(5, "bf")
print("Sleeping")
time.sleep(10)
print("Sleep Done")
handler.stopSerialListen()