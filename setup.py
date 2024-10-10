import requests
import socket

class Client:
    def __init__(self):
        ip = socket.gethostbyname(socket.gethostname())
        self.addr = "http://"+ ip +":8081/?payload="

    def sendAndGetLen(self,payload):
        payload = self.addr + payload
        return requests.get(payload).content.decode()

import deflate

a= "1234567letokenestlaréponsesuivante:1234567l"
b = deflate.deflate_compress(a.encode(), 6)

print(b)
print(len(b))