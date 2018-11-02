#!/usr/bin/python
# This script is for Car 3.
#This script is like ReceiverSendBackFile.py except that it receives and sends back twice since it's in the middle
#It waits to receive a message then sends a message back

import socket
import datetime

def Main():
        #This section needs to be edited according to the car number
        listeningPort = 5003 #Car1 is 5001, Car2 is 5002, Car3 is 5003, etc...
        hostLower = '192.168.1.12' #Send back to this IP. Car1 is ..1.11, Car2 is ...1.12, Car3 is 1.13, etc...
        portLower = 5002
        hostUpper = '192.168.1.14' #Pass message on (send) to this IP
        portUpper = 5004
        #End of section that needs to be edited

        expectedFileSize = 4096
        print("starting...")

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        data = ""
        while True:
                data = mySocket.recv(expectedFileSize).decode() #receive message
                print("Received file length "+str(len(data)))
                mySocket.sendto(data.encode(),(hostUpper,int(portUpper))) #Pass message on to the "Upper" host
                # Wait for a message back from the upper host
                data = mySocket.recv(expectedFileSize).decode() #receive message
                print("Received file length "+str(len(data)))
                #Send back to the lower host
                mySocket.sendto(data.encode(),(hostLower,int(portLower))) #Send back to the "Lower" host

        mySocket.close()

if __name__ == '__main__':

    Main()
