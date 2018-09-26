import socket
import datetime
 
def Main():
        listeningPort = input("Enter listening port: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        data = ""
        while data != 'q':
            data = mySocket.recv(512).decode()
            print ("Time Recvd:"+datetime.datetime.now().strftime("%H:%M:%S.%f")+", "+data)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
