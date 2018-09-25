import socket
 
def Main():
        host = input("Enter IP to send to: ")
        port = input("Enter Port to send to: ")
        print("starting...")
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        filename = input("Name of file to send: ")
        filehandle=open(filename,"rb")
        message=filehandle.read(1024)
        mySocket.sendto(message,(host,int(port)))       
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
