from socket import *
from dolarAPI import *
import json  # Importar el módulo json para serializar y deserializar

class UDPServer:
    __port: int
    __serverSocket: any

    def __init__(self, port):
        self.__port = port

    def createSocket(self):
        self.__serverSocket = socket(AF_INET, SOCK_DGRAM) #SOCKDGRAM: UDP
        self.bindSocket()

    def bindSocket(self):
        try:
            self.__serverSocket.bind(('', self.__port))
            print('El Servidor está listo y escuchando en el puerto: {}'.format(self.__port))
        except Exception as e:
            print(f'Error: {e}')

    def receiveMessage(self):
        while True:
            message, clientAdress = self.__serverSocket.recvfrom(2048)  # Leerá hasta 2048 Bytes (Tamaño del buffer)
            print(f"Mensaje recibido: {message.decode()} de {clientAdress}")
            dolar = dolarAPI()
            
            if(message.decode() == 'Dólar Oficial'):
                response_dict = dolar.getDolarOficial()  # Obtener el dict de la API
                
            elif(message.decode() == 'Dólar Blue'):
                response_dict = dolar.getDolarBlue()
                
            elif(message.decode() == 'Dólar Tarjeta'):
                response_dict = dolar.getDolarCard()
                
            elif(message.decode() == 'Dólar Cripto'):
                response_dict = dolar.getDolarCripto()

            response_json = json.dumps(response_dict)  # Serializar el dict a JSON
            response_bytes = response_json.encode('utf-8')  # Convertir la cadena JSON a bytes
            print(f"Mensaje enviado: {response_dict}")
            self.sendMessage(response_bytes, clientAdress)

    def sendMessage(self, message, clientAdress):
        self.__serverSocket.sendto(message, clientAdress)
