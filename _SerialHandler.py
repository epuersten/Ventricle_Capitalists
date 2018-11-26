import serial
import threading
import struct


#Thread that handles non-blocking polling from the serial port
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
        self.running = False #Global variable that specifies whether or not the thread is still running...
                            #We set this to false from SerialHandler when we want to stop polling

    #The polling thread
    def run(self):
        self.port.reset_input_buffer()
        while self.running:
            self.__serialRead()



    def __serialRead(self):
        pos = 0;  # Position in the read byte array
        orderPos = 0  # Position in the input order
        output = []
        dataIn = b''

        # print(self.port.in_waiting)
        # self.port.reset_input_buffer()

        # first try to read in the data. Read as many bytes as were specified
        # +1 represents the newline terminator
        # if True:
        while (len(dataIn) < self.numInputs + 1):
            try:
                # dataIn = self.port.read(self.numInputs)
                dataIn += (self.port.read())
                if(dataIn[-1] == 10):
                    break
            # RETURN NONE IF THE SERIAL BREAKS
            except serial.SerialException:
                self.callback(None)
                return
        # dataIn = self.port.read(self.numInputs)
        print(dataIn)

        if(len(dataIn) - 1 < self.numInputs):
            print("SKIPPING")
            return

        # if(True):
        try:  # In case the caller puts the wrong data input
            # Then depack it one packet at a time
            while pos < self.numInputs:
                if (self.inputOrder[orderPos] == 'h'):  # If we have a byte packet, treat as one byte and store
                    output += (struct.unpack('' + self.inputOrder[orderPos], dataIn[pos:pos + 2]))
                    pos += 2  # Advance to next position
                elif (self.inputOrder[
                          orderPos] == 'f'):  # If we have a float packet, read in the next 4 bytes and store
                    output += (struct.unpack('' + self.inputOrder[orderPos], dataIn[pos:pos + 4]))
                    pos += 4  # ditto
                orderPos = orderPos + 1

                # If we're not outputting to the EGram window, write to console
            if (self.callback == None):
                print(output)
            else:
                self.callback(output)
        except:
            print("Improper layout/number of bytes provided!")

class SerialHandler:

    #Constructor that creates the COM port with a specified address
    def __init__(self, comport):
        self.port = serial.Serial(comport, 19200, timeout=1)         #Serial port to do comms on
        self.serialThread = None #Thread declaration for later...
        self.polling = False

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

    #Stops the polling thread from listening to the port
    def stopSerialListen(self):
        if(self.polling == True):
            self.polling = False
            self.serialThread.running = False
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
        self.serialThread = serialReadThread(numPoints, order, self.port, callback)

        #Starts serial if not already started
        if (self.port.isOpen() == False):
            self.port.open()

        #Notify that we are polling
        self.polling = True
        
        #Then starts reading thread
        self.serialThread.running = True
        self.serialThread.start()

    #Close the serial port
    def close(self):
        self.port.close()
