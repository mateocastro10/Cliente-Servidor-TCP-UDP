from socket import * 
import json
class UDPConfig:

    __port : int
    __clientSocket : any
    __serverName : str
    
    def __init__(self,port, ip):
        self.__port = port
        self.__serverName = ip
        
    def createSocket(self):
        self.__clientSocket = socket(AF_INET,SOCK_DGRAM)
    
    def sendMessage(self,message):
        self.__clientSocket.sendto(message.encode(),(self.__serverName, self.__port))
        
    def receiveMessage(self):
        message, serverAdress =  self.__clientSocket.recvfrom(2048)
        response_json = message.decode('utf-8')  # Decodificar de bytes a cadena
        response_dict = json.loads(response_json)  # Deserializar la cadena JSON a un dict
        return (response_dict)
    
    def close(self):
        self.__clientSocket.close()
        