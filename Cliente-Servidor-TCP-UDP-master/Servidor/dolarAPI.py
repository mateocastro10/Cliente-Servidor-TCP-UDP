import requests

class dolarAPI():    
    
    __url : str
    
    def __init__(self):
        self.__url = 'https://dolarapi.com/v1/'
        
    def getDolarOficial(self):
        localUrl = self.__url + 'dolares/oficial'
        print(localUrl)
        response = requests.get(localUrl)
        return response.json()


    
    