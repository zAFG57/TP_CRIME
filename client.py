from flask import Flask, request
import requests
import deflate
import logging
import socket

log = logging.getLogger('werkzeug')
log.disabled = True

ip = socket.gethostbyname(socket.gethostname())
server = "http://"+ip+":8080/"
MITM = "http://"+ip+":8082/"
mdpUser = "mdp super secret de l'uttilisateur (c'est pas ça qu'on cherche)"
SECRET = requests.get(server+mdpUser).content.decode()
HEADERS = "secret=" + SECRET + "inserez des text peut importe"

app = Flask(__name__)

@app.route("/",methods=['GET'])
def reponse():
    payload = request.args.get('payload')
    if payload == None:
        return "ip:port/?payload=... il faut lire le sujet"

    req = HEADERS + "&secret=" + payload
    reqComp = deflate.deflate_compress(req.encode(), 6)
    response = requests.get(MITM+str(reqComp).replace("b'","").replace("'","").replace("/","_"))
    nb = int(response.content.decode())
    return str(nb)

app.run(host=ip, port=8081)

