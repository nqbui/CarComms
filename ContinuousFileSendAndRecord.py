#!/usr/bin/python
import socket
import datetime
import time
 
def Main():
        expectedFileSize=65536
        filepath='/home/pi/Documents/CarCommsData/dataRecorded1.txt'
        dataRecordFile=open(filepath,'a')
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        listeningPort = input("Enter listening port: ")
        filename = input("Name of file to send: ")
        filehandle=open(filename,"rb")
        message=filehandle.read(expectedFileSize)
        messageLength=str(len(message))
        distance=input("Enter distance: ")
        speed=input("Enter speed: ")
        print("starting...")
        dataRecv=""
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        for x in range(0,10): # x will go from 0 to less than the second number
                dataRecordFile.write(str(x) +","+ datetime.datetime.now().strftime("%H:%M:%S.%f"))
                mySocket.sendto(message,(host,int(port)))
                dataRecv = mySocket.recv(expectedFileSize)
                dataRecordFile.write(","+ datetime.datetime.now().strftime("%H:%M:%S.%f")+","+distance+","+speed+","+messageLength+"\r\n")
                time.sleep(.5) #wait .5 secs

        message="q"
        mySocket.sendto(message.encode(),(host,int(port)))
        mySocket.close()
        
        dataRecordFile.close()
 
if __name__ == '__main__':
    Main()
