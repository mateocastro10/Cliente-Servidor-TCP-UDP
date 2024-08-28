from socket import *

class TCPServer:
    __port: int
    __serverSocket: any

    def __init__(self, port):
        self.__port = port
        
    def createSocket(self):  # Crea el socket para el servidor
        self.__serverSocket = socket(AF_INET, SOCK_STREAM)  # AF_INET es para IPv4, SOCK_STREAM es para TCP
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
            
            message = connectionSocket.recv(2048)  # Lee hasta 2048 bytes (tamaño del buffer)
            if not message:
                break
            
            print(f"Mensaje recibido: {message.decode()} de {addr}")
            modifiedMessage = message.decode().upper()
            self.sendMessage(modifiedMessage.encode(), connectionSocket)
            print(f'Mensaje enviado: {modifiedMessage}')
            connectionSocket.close()  # Cierra la conexión

    def sendMessage(self, message, connectionSocket):
        connectionSocket.send(message)  # Envía el mensaje a través de la conexión aceptada
