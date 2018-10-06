import socket
import datetime
import time
 
def Main():
        filepath='/home/pi/Documents/CarCommsData/dataRecorded1.txt'
        dataRecordFile=open(filepath,'w')
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        listeningPort = input("Enter listening port: ")
        print("starting...")
        messageToSend=""
        dataRecv=""
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        for x in range(0,10):
                dataRecordFile.write(str(x) +","+ datetime.datetime.now().strftime("%H:%M:%S.%f"))
                messageToSend="Nam Bui testing"
                mySocket.sendto(messageToSend.encode(),(host,int(port)))
                dataRecv = mySocket.recv(512).decode()
                dataRecordFile.write(","+ datetime.datetime.now().strftime("%H:%M:%S.%f")+"\r\n")
                time.sleep(.5) #wait .5 secs

        messageToSend="q"
        mySocket.sendto(messageToSend.encode(),(host,int(port)))
        mySocket.close()
        
        dataRecordFile.close()
 
if __name__ == '__main__':
    Main()
