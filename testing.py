from SerialHandler import *
import time

handler = SerialHandler("COM12")

handler.sendData("Hello world")

handler.startSerialListen()
time.sleep(10)
handler.stopSerialListen()