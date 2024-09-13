from socket import *
import json
class TCPConfig:
    __port: int
    __clientSocket: any
    __serverName: str
    
    def __init__(self, port, ip):
        self.__port = port
        self.__serverName = ip
        self.__clientSocket = None

    def createSocket(self):
        self.__clientSocket = socket(AF_INET, SOCK_STREAM)
        self.__clientSocket.connect((self.__serverName, self.__port))
    
    def sendMessage(self, message):
        self.__clientSocket.send(message.encode())

    def receiveMessage(self):
        message, serverAdress =  self.__clientSocket.recv(2048)
        response_json = message.decode('utf-8')  # Decodificar de bytes a cadena
        response_dict = json.loads(response_json)  # Deserializar la cadena JSON a un dict
        return (response_dict)

    def closeSocket(self):
        self.__clientSocket.close()

