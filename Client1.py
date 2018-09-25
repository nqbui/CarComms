import socket
 
def Main():
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        message = input("Type message to send: ")
         
        while message != 'q':
            mySocket.sendto(message.encode(),(host,int(port)))       
            message = input("Type message to send: ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
