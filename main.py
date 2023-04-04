# https://codeavecjonathan.com/res/programmation.txt

# https://codeavecjonathan.com/res/exemple.html
#https://codeavecjonathan.com/res/papillon.jpg

import requests
import json



reponse=requests.get("https://codeavecjonathan.com/res/pizzas1.json")
if reponse.status_code==200:
    pizzas=json.loads(reponse.text)
    print(str(len(pizzas)))
    print(reponse.text)
else:
    print("Erreur de code : " +reponse.status_code)


reponseimage=requests.get("https://codeavecjonathan.com/res/papillon.jpg")

if reponseimage.status_code==200:
    f=open("papillon.jpg", "wb")
    f.write(reponseimage.content)
    f.close

else:
    print("Erreur reponse : "+reponseimage.status_code)

