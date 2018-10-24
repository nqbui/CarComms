#This script acts just like a server
#It waits to receive a message then sends a message back
import socket
import datetime

 
def Main():
        listeningPort = input("Enter listening port: ")
        host = input("Enter IP to send back to: ")
        port = input("Enter Port to send back to: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        data = ""
        while data != 'q':
                data = mySocket.recv(65536).decode()
                print("Received file length "+str(len(data)))
                mySocket.sendto(data.encode(),(host,int(port)))     
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()


