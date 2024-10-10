# TP CRIME (~30 Minutes):

## Installation du TP :

Premièrement, il faut cloner le repo git: [https://github.com/zAFG57/TP_CRIME](https://github.com/zAFG57/TP_CRIME).

Une fois que vous avez cloné le tp, vous devez créer un environnement virtuel python grâce à la commande suivante: ```virtualenv tp```.

Vous devez ensuite activer cet environnement virtuel grâce à cette commande : ```. ./tp/bin/activate```

Vous devez ensuite télécharger via l'outil pip les paquets qui nous seront essentiels pour la suite du tp:
```
pip install deflate
pip install flask
pip install requests
```
Enfin, la dernière étape est le lancement des scripts déjà écrit pour vous :
```
python3 server.py& python3 client.py& python3 ManInTheMiddle.py&
```
<sub>*(à noter que ces scripts fonctionnent en background donc si vous les modifier pour faire des tests, vous devez les kill avant de les relancer)*</sub>

## Ce qui existe déjà :

Dans ce tp, le but est de comprendre le mécanisme qui permet à l'attaque **CRIME** de fonctionner. Ainsi, plusieurs élément annexe de l'attaque sont déjà mis en place pour vous. En effet, il existe déjà :
- un serveur web qui :
    - Envoie un token lorsque le client envoie son mot de passe via l'adresse suivante : ```http://ip:8080/[motsdepasse]```
    - Possède une page ou l'on doit être authentifier avec le token via l'address suivante: ```http://ip:8080/?token=[le token]```
- un client qui:
    - Possède un mot de passe et qui récupère son token dès le lancement du script
    - Est victime d'une attaque man in the middle
    - Envoie des requêtes au serveur sur commande suite à l'exploitation d'une faille hypothétique (comme par exemple si l'on avait profité de l'attaque man in the middle pour envoyer un script javascript pour qu'il s'éxectute sur le navigateur du client).
- une partie du script de l'attaquant qui :
    - vous indique la taille des requêtes que le client envoie au serveur après la compression et le chiffrement.
    - possède une méthode pour contacter le client et lui demander d'effectuer une requête au serveur en ajoutant le texte de votre choix à la fin (sans que vous n'ayez la main sur le contenu de la requête).

## Ce que vous devez faire pour ce TP :

Vous devez compléter le fichier attaque.py pour qu'il mette en place l'attaque en utilisant les différentes briques à votre disposition. Ce script doit vous retourner le token du client. Pour cela, vous devez faire envoyer des requêtes au client et à partir des informations sur la taille des paquets, retrouver petit à petit le token. Une fois que vous avez obtenu le token, vous pouvez vérifier que le token est correct en vous rendant sur la page suivante : ```ip:8080/?token=[le token]```. À noter que le token est une suite de 10 chiffres.
### Bonus: 
Si vous avez du temps, vous pouvez également automatiser la vérification du token en utilisant la librairie requests de python.

## Piège à éviter <sub>*(pas obligatoire pour réaliser le TP)*</sub> :

Lorsque vous essayez de trouver le token, il est possible que vous ne trouviez pas qu'un seul caractère qui lorsqu'on l'ajoute à la requête compressée, réduis ou maintien sa taille.
Vous devez donc prendre en compte cette information pour mener à bien l'attaque et garantir de trouver à chaque fois correctement tous les caractères du token.

## Rappel de cour :

L'attaque CRIME est une attaque par canal auxiliaire. En effet, elle n'exploite pas de faille dans l'algorithme de compression deflate ou dans TLS/SSL, mais elle repose sur l'utilisation de données indirectes. L'attaque CRIME est possible sur les communications utilisant TLS(1.0 et 1.1) et SSL 3.0 lorsque la compression est activée (deflate). Pour réaliser l'attaque, vous devez avoir accès à la taille des requêtes (compressé et chiffré) envoyé par votre victime et vous devez avoir la main sur une partie de cette requête avant la compression et le chiffrement. Pour deviner une partie de la requête comme un token de connexion, vous pouvez deviner un par un tout les caractères du token. Cela marche, car l'algorithme de compression deflate réduis la taille de la requête plus il y a de répétition et qu'il y a une correspondance directe entre la taille de la requête compressé et compressé/chiffré. Ainsi, vous pouvez écrire des caractères en plus dans la requête et en observant la taille de la requête, vous êtes capable de déterminer si elle possède des répétitions ou non et ainsi déterminer petit à petit le token.

*crée par: **Ludovic CASTIGLIA**, **Maxime ROUDIER**, **Noa SILLARD**, **Lucie GOIGOUX**, **Loris OBRY***