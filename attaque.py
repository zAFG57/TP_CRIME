import setup
import requests
import string

client = setup.Client()

#############################################################################################################
#                                                                                                           #
#    la commande:                                                                                           #
#        client.sendAndGetLen("")                                                                           #
#    demande à votre victime d'envoyé une requête au serveur (contenant le token que vous devez deviner)    #
#    en ajoutant la chaîne de caractère entre "" et vous renvoie la taille de la requête après              #
#    compression et chiffrement calculé grâce à l'attaque Man in the middle.                                #
#                                                                                                           #
#############################################################################################################

# TODO: crée une fonction de manière itératif ou récursif (au choix) qui retourne les tokens potentiels








# Bonus: Crée une fonction qui trie les tokens potentiels du vrai token en essayant de se connecter.

server = "http://"+socket.gethostbyname(socket.gethostname())+":8080/?token="

#################################################################################
#                                                                               #
#    la commande:                                                               #
#        requests.get(server).content.decode()                                  #
#    Retourne la page que retourne le site lorsque le token n'est pas le bon.   #
#    Pour tester si le token est le bon, vous devez l'ajouter à la route        #
#                                                                               #
#################################################################################

