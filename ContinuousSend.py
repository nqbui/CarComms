import socket
import datetime
import time
 
def Main():
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for x in range(0,120):
                message="#" + x + ", Time sent: " + datetime.datetime.now().strftime("%H:%M:%S.%f")
                mySocket.sendto(message.encode(),(host,int(port)))       
                time.sleep(.5) #wait .5 secs
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
