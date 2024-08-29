import requests

class dolarAPI():    
    
    __url : str
    
    def __init__(self):
        self.__url = 'https://dolarapi.com/v1/'
        
    def getDolarOficial(self):
        localUrl = self.__url + 'dolares/oficial'
        response = requests.get(localUrl)
        return response.json()

    def getDolarBlue(self):
        localUrl = self.__url + 'dolares/blue'
        response = requests.get(localUrl)
        return response.json()

    def getDolarCripto(self):
        localUrl = self.__url + 'dolares/cripto'
        response = requests.get(localUrl)
        return response.json()
    
    def getDolarCard(self):
        localUrl = self.__url + 'dolares/tarjeta'
        response = requests.get(localUrl)
        return response.json()
    
    