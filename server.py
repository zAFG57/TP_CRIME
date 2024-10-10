from flask import Flask, request
import logging
import random
import socket

ip = socket.gethostbyname(socket.gethostname())
log = logging.getLogger('werkzeug')
log.disabled = True

SECRET = str(random.randint(1000000000,9999999999))
mdpUser = "mdp super secret de l'uttilisateur (c'est pas ça qu'on cherche)"

app = Flask(__name__) 

@app.route("/",methods=['GET'])
def reponse():
    a = request.args.get('token')
    if a==SECRET:
        return "bienvenu garçon"
    return "pas autentifié"

@app.route("/<mdp>",methods=['GET'])
def creationToken(mdp):
    if (mdp == mdpUser):
        return SECRET
    return str(random.randint(1000000000,9999999999))

app.run(host=ip, port=8080)