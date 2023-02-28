# unitTestAPI

## Pré requis et installation

Cette APi fonctionne avec MONGODB, une fois fastAPI lancer celle-ci va se créer toute seul.

Pour l'installation vous aurez besoin de différent ne commençant par "pip install", faites ceux-ci pour chacun des packages suivants : fastapi, uvicorn, unitest, requests

exemple : 

`````
pip install fastapi
`````

## Utilisation

Pour utiliser cette API vous devez la lancer avec cette commande :

``````
python app/main.py
``````
Puis avec votre navigateur préféré aller sur l'url ci-dessous
``````
http://127.0.0.1:8000/
``````

## Test

Pour lancer veuillez excuter cette commande :
````
cd test/unit/app
python -m unittest -v apiTest
````