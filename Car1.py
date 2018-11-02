#!/usr/bin/python
# This script is for Car 1. Sends to and receives from Car 2.
import socket

import datetime

import time

 

def Main():

        expectedFileSize=4096 #expect a max file size of 4 kilobytes

        filepath='/home/pi/Documents/CarCommsData/dataRecorded1.txt'

        dataRecordFile=open(filepath,'a')

        host = '192.168.1.12' #Car 2 IP

        port = 5002 #Car 2 port num

        listeningPort = 5001 #Car 1 port num (what Car 1 is listening to)

        filename = 'largefile.txt' #largefile.txt is a 1.47kb text file

        filehandle=open(filename,"rb")

        message=filehandle.read(expectedFileSize)

        messageLength=str(len(message))

        distance=input("Enter distance: ")

        #speed=input("Enter speed: ")#NO SPEED ENTRY

        print("starting...")

        dataRecv=""

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        mySocket.bind(('0.0.0.0', int(listeningPort)))

        for x in range(0,5): # x will go from 0 to less than the second number

                timeNow = datetime.datetime.now()

                dataRecordFile.write(str(x) +","+ timeNow.strftime("%H:%M")+","+timeNow.strftime("%S.%f"))

                mySocket.sendto(message,(host,int(port)))

                dataRecv = mySocket.recv(expectedFileSize)

                timeNow = datetime.datetime.now()

                dataRecordFile.write(","+ timeNow.strftime("%H:%M")+","+timeNow.strftime("%S.%f")+","+distance+","+messageLength+"\r\n")

                time.sleep(1) #wait 1 secs

        message="q"

        mySocket.sendto(message.encode(),(host,int(port)))

        mySocket.close()

        dataRecordFile.close()

 

if __name__ == '__main__':

    Main()
