import serial
import threading
import struct
import time

#Thread that handles non-blocking reading fro mthe serial port
class serialReadThread(threading.Thread):
    def __init__ (self, number, order, port, targetWindow = None):
        threading.Thread.__init__(self)
        self.numInputs = number
        self.inputOrder = order
        self.port = port
        self.targetWindow = targetWindow

    #The reading thread
    def run(self):
        pos = 0; #Position in the read byte array
        orderPos = 0 #Position in the input order
        output = []
        dataIn = b''

        #first try to read in the data. Read as many bytes as were specified
        while(len(dataIn) < self.numInputs):
            dataIn += (self.port.read())
            #print("RECIEVED")

        print(dataIn)

        #if(True):
        try:#In case the caller puts the wrong data input
            #Then depack it one packet at a time
            while pos < self.numInputs:
                if(self.inputOrder[orderPos] == 'h'): #If we have a byte packet, treat as one byte and store
                    output += (struct.unpack(self.inputOrder[orderPos], dataIn[pos:pos+2]))
                    pos += 2 #Advance to next position
                elif (self.inputOrder[orderPos] == 'f'): #If we have a float packet, read in the next 4 bytes and store
                    output += (struct.unpack(self.inputOrder[orderPos], dataIn[pos:pos+4]))
                    pos += 4 #ditto
                #print(output)
                orderPos = orderPos + 1

                #If we're not outputting to the EGram window, write to console
            if(self.targetWindow == 0):
                print(output)
        except:
            print("Improper layout/number of bytes provided!")
        
        self.port.flush()

class SerialHandler:

    #Constructor that creates the COM port with a specified address
    def __init__(self, comport):
        self.port = serial.Serial(comport, 9600, timeout=1)         #Serial port to do comms on
        self.inputOrder = ""
        self.numInputs = 0
        self.polling = False #Defines whether or not we're polling for data right now
        self.serialThread = None #Thread declaration for later...

    #Connect to port and send the data.
    #ToDo: Add try/catch and error checking
    def sendData(self, toSend): 
        if(self.port.isOpen() == False):   
            self.port.open()     #Open serial port only when transmitting
            time.sleep(2)

        for data in toSend:  #Send all data to the pacemaker
            #Convert to either uint16 or float
            try:
                self.port.write(struct.pack("h", int(data))) 
                #print("byte")
            except: #If conversion to int is unsuccessful, it must be a float. Try to send that instead.
                self.port.write(struct.pack("f", float(data)))
                #print("float")
        self.port.write("\n".encode()) #End off with a newline

    #Stops the polling thread from listening to the port
    def stopSerialListen(self):
        if(self.polling == True):
            self.polling = False
            self.serialThread.join()
            self.port.close()
        
    #Starts the serial thread that continuously reads in sensor data from the pacemaker
    #numPoints is the total amount of bytes to read in
    #order is the order of variables to send in, as a string.
    #Based on this order, the method will automatically
    #'dissect' the input to return an output collection
    #Target is the ECG windows to supply the target too, but that can be left blank to get
    #raw console output.
    def startSerialListen(self, numPoints, order, target=0):
        #Update local instances of these values
        self.inputOrder = order
        self.numInputs = numPoints
        self.targetWindow = target
        self.serialThread = serialReadThread(numPoints, order, self.port, target)

        #Starts serial if not already started
        if (self.port.isOpen() == False):
            self.port.open()
            time.sleep(2)

        #Notify that we are polling
        self.polling = True
        
        #Then starts reading thread
        self.serialThread.start()

    #Close the serial port
    def close(self):
        self.port.close()
