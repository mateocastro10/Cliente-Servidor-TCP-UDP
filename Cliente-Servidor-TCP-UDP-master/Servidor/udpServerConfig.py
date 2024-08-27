from socket import *
import http.client

class UDPServer:
    
    __port : int
    __serverSocket : any
    #__serverip: str

    def __init__(self):
        self.__port = 12000
        
        
    def createSocket(self):
        self.__serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.bindSocket()

    def bindSocket(self):
        try:
            self.__serverSocket.bind(('',self.__port))
            print('El Servidor esta listo y escuchando en el puerto: {}'.format(self.__port))
        except Exception as e:
            print(f'Error: {e}')
            
    def receiveMessage(self):
        while True:
            message,clientAdress = self.__serverSocket.recvfrom(2048) #Leera hasta 2048 Bytes (Tamaño del buffer)
            print(f"Mensaje recibido: {message.decode()} de {clientAdress}")
            modifiedMessage = message.decode().upper()
            self.sendMessage(modifiedMessage.encode(),clientAdress)
            
    def sendMessage(self,message,clientAdress):
        self.__serverSocket.sendto(message,clientAdress)
        