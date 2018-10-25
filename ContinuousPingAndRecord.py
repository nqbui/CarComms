#!/usr/bin/python
import socket
import datetime
import time
 
def Main():
        filepath='/home/pi/Documents/CarCommsData/dataRecorded1.txt'
        dataRecordFile=open(filepath,'a')
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        listeningPort = input("Enter listening port: ")
        messageToSend=input("Enter a message to send: ")
        messageLength=str(len(messageToSend))
        distance=input("Enter distance: ")
        speed=input("Enter speed: ")
        print("starting...")
        dataRecv=""
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        for x in range(0,10): # x will go from 0 to less than the second number
                dataRecordFile.write(str(x) +","+ datetime.datetime.now().strftime("%H:%M:%S.%f"))
                mySocket.sendto(messageToSend.encode(),(host,int(port)))
                dataRecv = mySocket.recv(512).decode()
                dataRecordFile.write(","+ datetime.datetime.now().strftime("%H:%M:%S.%f")+","+distance+","+speed+","+messageLength+"\r\n")
                time.sleep(.5) #wait .5 secs

        messageToSend="q"
        mySocket.sendto(messageToSend.encode(),(host,int(port)))
        mySocket.close()
        
        dataRecordFile.close()
 
if __name__ == '__main__':
    Main()
