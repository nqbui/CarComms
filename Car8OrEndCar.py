#!/usr/bin/python
# This script is for Car 8 or whatever the car at the end of the train is.
#This script is like ReceiverSendBackFile.py
#It waits to receive a message then sends a message back

import socket
import datetime
 

def Main():

        listeningPort = 5008 #listening port number for Car8
        host = '192.168.1.17' #See Interim Report for IP and Port number assignments #input("Enter IP to send back to: ")
        port = 5007 #input("Enter Port to send back to: ")

        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        data = ""
        while True:
                data = mySocket.recv(4096).decode()
                print("Received file length "+str(len(data)))
                mySocket.sendto(data.encode(),(host,int(port)))                   

        mySocket.close() 

if __name__ == '__main__':

    Main()

