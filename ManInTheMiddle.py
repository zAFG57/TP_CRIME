from flask import Flask
import logging
import socket

log = logging.getLogger('werkzeug')
log.disabled = True
app = Flask(__name__)
ip = socket.gethostbyname(socket.gethostname())

@app.route("/<payload>",methods=['GET'])
def attaque(payload):
    return str(len(payload))

app.run(host=ip, port=8082)