from socket import *

class TCPConfig:
    __port: int
    __clientSocket: any
    __serverName: str
    
    def __init__(self, port: int):
        self.__port = port
        self.__serverName = 'localhost'
        self.__clientSocket = None

    def createSocket(self):
        self.__clientSocket = socket(AF_INET, SOCK_STREAM)
        self.__clientSocket.connect((self.__serverName, self.__port))
    
    def sendMessage(self, message):
        self.__clientSocket.send(message.encode())

    def receiveMessage(self):
        return self.__clientSocket.recv(2048).decode()

    def closeSocket(self):
        self.__clientSocket.close()

