from socket import * 

class UDPConfig:

    __port : int
    __clientSocket : any
    __serverName : str
    
    def __init__(self,port: int):
        self.__port = port
        self.__serverName = 'localhost'
        
    def createSocket(self):
        self.__clientSocket = socket(AF_INET,SOCK_DGRAM)
    
    def sendMessage(self,message):
        self.__clientSocket.sendto(message.encode(),(self.__serverName, self.__port))
        
    def receiveMessage(self):
        message, serverAdress =  self.__clientSocket.recvfrom(2048)
        return (message.decode())
    
    def close(self):
        self.__clientSocket.close()
        