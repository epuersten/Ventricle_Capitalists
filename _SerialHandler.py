import serial
import threading
import struct
import time



#To handle ECG input we can do things in two ways
# >Ping the pacemaker and ask for input
# >Continuously receive data from the pacemaker
# The pacemaker will send data back as floats.

#Thread that handles non-blocking reading fro mthe serial port
class serialReadThread(threading.Thread):
    #TODO: Add a callback function parameter
    #The callback function is passed the data received from the thread
    #Then, the function in EGram window should update the screen based on 
    #What data is collected from the thread
    def __init__ (self, number, order, port, callback = None):
        threading.Thread.__init__(self)
        self.numInputs = number
        self.inputOrder = order
        self.port = port
        self.callback = callback

    #The reading thread
    def run(self):
        pos = 0; #Position in the read byte array
        orderPos = 0 #Position in the input order
        output = []
        dataIn = b''

        #first try to read in the data. Read as many bytes as were specified
        while(len(dataIn) < self.numInputs):
            try:
                dataIn += (self.port.read())
            #RETURN NONE IF THE SERIAL BREAKS
            except serial.SerialException:
                self.callback(None)
                return
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
                orderPos = orderPos + 1

                #If we're not outputting to the EGram window, write to console
            if(self.callback == None):
                print(output)
            else:
                print(output)
                self.callback(output)
        except:
            print("Improper layout/number of bytes provided!")
        
        self.port.reset_input_buffer()

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

        for data in toSend:  #Send all data to the pacemaker
            #Convert to either int16 or float
            try:
                self.port.write(struct.pack("<h", int(data))) 
                print("short")
                print(struct.pack("<h", int(data)))
            except: #If conversion to int is unsuccessful, it must be a float. Try to send that instead.
                self.port.write(struct.pack("<f", float(data)))
                print("float")
        #self.port.write("\n".encode()) #End off with a newline

    #Stops the polling thread from listening to the port
    def stopSerialListen(self):
        if(self.polling == True):
            self.polling = False
            self.serialThread.join()
            #self.port.close()
        
    #Starts the serial thread that continuously reads in sensor data from the pacemaker
    #numPoints is the total amount of bytes to read in
    #order is the order of variables to send in, as a string.
    #Based on this order, the method will automatically
    #'dissect' the input to return an output collection
    #Target is the ECG windows to supply the target too, but that can be left blank to get
    #raw console output.
    def startSerialListen(self, numPoints, order, callback):
        #Update local instances of these values
        self.inputOrder = order
        self.numInputs = numPoints
        self.serialThread = serialReadThread(numPoints, order, self.port, callback)

        #Starts serial if not already started
        if (self.port.isOpen() == False):
            self.port.open()
            time.sleep(2)

        #Notify that we are polling
        self.polling = True
        
        #Then starts reading thread
        self.serialThread.start()

    #Reconnection method. To be used in the event that a device is disconnected...
    #def reconnect(self):
    #    curPort = self.port.name
    #    self.port.close()
    #    self.port = None
    #    self.port = serial.Serial(curPort, 9600, timeout=1) #Close and re-open the port
    #    self.port.open()

    #Close the serial port
    def close(self):
        self.port.close()
