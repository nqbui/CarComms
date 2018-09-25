import socket
 
def Main():
        listeningPort = input("Enter listening port: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySocket.bind(('0.0.0.0', int(listeningPort)))
        data = mySocket.recv(512).decode()
        while data != 'q':
            print ('Received from server: ' + data)
            data = mySocket.recv(512).decode()
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
