import serial
import threading
import struct

class SerialHandler:
    

    #Constructor that creates the COM port with a specified address
    def __init__(self, comport):
        self.port = serial.Serial()         #Serial port to do comms on
        self.port.baudrate = 9600           #Baud Rate for the port. MUST BE THE SAME AS THE PACEMAKER OR IT WILL LOCK UP
        self.port.port = comport            #Define COM port to be used
        self.port.timeout = 5              #Automatic timeout when reading
        self.inputOrder = ""
        self.numInputs = 0
        self.targetWindow = 0
        self.enabled = 0 #Defines whether or not serial out put is enabled. If not, we have to before performing any operations
        self.polling = 0 #Defines whether or not we're polling for data right now
        self.serialThread = threading.Thread(target=readData)

    #Connect to port and send the data.
    #ToDo: Add try/catch and error checking
    def sendData(self, toSend): 
        
        if(self.enabled == 0)   
            self.port.open()     #Open serial port only when transmitting

        for data in toSend:  #Send all data to the pacemaker
            #Convert to either single-byte or float
            try:
                self.port.write(struct.pack("b", int(data))) 
            except: #If conversion to int is unsuccessful, it must be a float. Try to send that instead.
                self.port.write(struct.pack("f", float(data)))
            self.port.write("\n".encode())
        #self.port.close()


    #Testing code please ignore
    def recData(self):
        for i in range(3):
            data = self.port.readline()
            data = data[:len(data)-2] #Strip off the \r\n line terminator
            result = 0
            #Attempt int conversion, otherwise float conversion
            try:
                result = struct.unpack("b", data)
            except:
                result = struct.unpack("f", data)
            print(result)

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

        #Starts serial if not already started
        if self.enabled == 0:
            self.port.open()

        #Enable polling
        self.polling = 1
        
        #Then starts reading thread
        self.serialThread.start()

    #Stops the polling thread from listening to the port
    def stopSerialListen(self):
        self.polling = 0
        self.serialThread.join()

    #Function to read in data points over serial
    def readData(self):
        pos = 0; #Position in the read byte array
        output = []

        dataIn = None

        #first try to read in the data
        while(polling == 1 and dataIn == None):
            dataIn = self.port.read(self.numInputs)

        #Check if the loop was exited due to failure to the ECG window being closed
        if(polling == 0):
            return

        try: #In case the caller puts the wrong data input
            #Then depack it one packet at a time
            while pos < self.numInputs:
                if(self.inputOrder[pos] == 'b'): #If we have a byte packet, treat as one byte and store
                    output.append(struct.unpack(inputOrder[pos], dataIn[pos]))
                    pos += 1 #Advance to next position
                else if (self.inputOrder(pos) == 'f'): #If we have a float packet, read in the next 4 bytes and store
                    output.append(struct.unpack(inputOrder[pos], dataIn[pos:pos+4]))
                    pos += 4 #ditto

                #If we're not outputting to the EGram window, write to console
            if(targetWindow == 0):
                print(output)
        except:
            print("Improper layout/number of bytes provided!")
        
        
    
