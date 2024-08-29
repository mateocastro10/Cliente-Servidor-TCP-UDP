from socket import *
from dolarAPI import *
import json
class TCPServer:
    __port: int
    __serverSocket: any

    def __init__(self, port):
        self.__port = port
        
    def createSocket(self):  # Crea el socket para el servidor
        self.__serverSocket = socket(AF_INET, SOCK_STREAM)
        self.__serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Permite reutilizar la dirección
        # AF_INET es para IPv4, SOCK_STREAM es para TCP
        self.bindSocket()  # Enlaza el socket al puerto

    def bindSocket(self): 
        try:
            self.__serverSocket.bind(('', self.__port))  # Enlaza el socket al puerto indicado
            self.__serverSocket.listen(1)  # Escucha conexiones entrantes, encolando hasta 1 conexión
            print(f'El Servidor está listo y escuchando en el puerto: {self.__port}')
        except Exception as e:
            print(f'Error: {e}')

    def receiveMessage(self):
        while True:
            connectionSocket, addr = self.__serverSocket.accept()  # Acepta una nueva conexión
            print('Got connection from', addr)
            
            message = connectionSocket.recv(2048)  # Leerá hasta 2048 Bytes (Tamaño del buffer)
            print(f"Mensaje recibido: {message.decode()} de {addr}")
            
            dolar = dolarAPI()  # Suponiendo que dolarAPI es una clase
            
            if message.decode() == 'Dólar Oficial':
                response_dict = dolar.getDolarOficial()  # Obtener el dict de la API
                
            elif message.decode() == 'Dólar Blue':
                response_dict = dolar.getDolarBlue()
                
            elif message.decode() == 'Dólar Tarjeta':
                response_dict = dolar.getDolarCard()
                
            elif message.decode() == 'Dólar Cripto':
                response_dict = dolar.getDolarCripto()

            
            response_json = json.dumps(response_dict)  # Serializar el dict a JSON
            response_bytes = response_json.encode('utf-8')  # Convertir la cadena JSON a bytes
            self.sendMessage(response_bytes, connectionSocket)
            print(f'Mensaje enviado: {response_bytes}')

    def sendMessage(self, message, connectionSocket):
        connectionSocket.send(message)  # Envía el mensaje a través de la conexión aceptada

if __name__ == "__main__":
    server = TCPServer(12000)
    server.createSocket()
    server.receiveMessage()
