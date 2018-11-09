import serial
import struct

class SerialHandler:
    

    #Constructor that creates the COM port with a specified address
    def __init__(self, comport):
        self.port = serial.Serial()   #Serial port to do comms on
        self.port.baudrate = 9600        #Baud Rate for the port. MUST BE THE SAME AS THE PACEMAKER OR IT WILL LOCK UP
        self.port.port = comport    #Define COM port to be used

    #Connect to port and send the data.
    #ToDo: Add try/catch and error checking
    def sendData(self, toSend):    
        self.port.open()     #Open serial port only when transmitting
        for data in toSend:  #Send all data to the pacemaker
            #Convert to either single-byte or float
            try:
                self.port.write(struct.pack("b", int(data))) 
            except: #If conversion to int is unsuccessful, it must be a float. Try to send that instead.
                self.port.write(struct.pack("f", float(data)))
            self.port.write("\n".encode())
        #self.port.close()

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
        self.port.close()