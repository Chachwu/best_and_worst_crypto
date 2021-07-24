import urllib.request
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
# url
urlpage =  'https://coinmarketcap.com/' 
print(urlpage)
# query the website and return the html to the variable 'page'
page = requests.get(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find('script', id = '__NEXT_DATA__',type = 'application/json')
coins = {}
coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

#prendre les changements sur 24h pour tous les coins
L = ['percentChange24h']
for i in range(len(listings)):
    d = str(listings[i]).split(',')
    I = []
    for j in d:
        if 'percentChange24h' in j:
            I.append(j)
    L.append(float(I[len(I)-1][21:]))
#prendre les changements sur 7 jours pour tous les coins
K = ['percentChange7d']
for i in range(len(listings)):
    d = str(listings[i]).split(',')
    I = []
    for j in d:
        if 'percentChange7d' in j:
            I.append(j)
    K.append(float(I[len(I)-1][20:]))
#prendre les noms des coins classé par rang
S = ['name']
for i in range(len(listings)):
    d = str(listings[i]).split(',')
    I = []
    for j in d:
        if 'name' in j:
            I.append(j)
    S.append(I[0][9:])

J = L[1:]
J.sort()#trier par performance sur 24h
dix_plus24h = J[(len(J)-10):] #selection des 10 plus performantes
dix_moins24h = J[:10]#selection des 10 moins performantes
names_plus = []
names_min = []
def doublons(l):
    L = []
    for i in range(len(l)):
        if l[i] not in l[(i+1):]:
            L.append(l[i])
    return(L)
dix_plus24h = doublons(dix_plus24h)
dix_moins24h = doublons(dix_moins24h)
#On retrouve les noms des coins les plus et les moins performantes sur 24h
for i in dix_plus24h:
    k = 0
    for j in L:
        if j == i:
            names_plus.append(S[k])
        else:
            k+=1
for i in dix_moins24h:
    k = 0
    for j in L:
        if j == i:
            names_min.append(S[k])
        else:
            k+=1
#Affichage des données sur 24h
Plus24 = ['les 10 coins qui ont le plus monte en 24h']
Moins24 = ['les 10 coins qui ont le plus baisse en 24h']
for i in range(10):
    Plus24.append(names_plus[9 - i] +':'+str(dix_plus24h[9-i])+'%')
    Moins24.append(names_min[i] +':'+str(dix_moins24h[i])+'%')
print(json.dumps(Plus24,indent = 4))
print(json.dumps(Moins24,indent = 4))
#Pour 7 jours
J = K[1:]
J.sort()#trier par performance sur 7 jours
dix_plus7d = J[(len(J)-10):] #selection des 10 plus performantes
dix_moins7d = J[:10]#selection des 10 moins performantes
names_plus7 = []
names_min7 = []
def doublons(l):
    L = []
    for i in range(len(l)):
        if l[i] not in l[(i+1):]:
            L.append(l[i])
    return(L)
dix_plus7d = doublons(dix_plus7d)
dix_moins7d = doublons(dix_moins7d)
#On retrouve les noms des coins les plus et les moins performantes sur 7 jours
for i in dix_plus7d:
    k = 0
    for j in L:
        if j == i:
            names_plus7.append(S[k])
        else:
            k+=1
for i in dix_moins7d:
    k = 0
    for j in L:
        if j == i:
            names_min7.append(S[k])
        else:
            k+=1
#Affichage des données sur 7 jours
Plus7 = ['les 10 coins qui ont le plus monte en 7 jours']
Moins7 = ['les 10 coins qui ont le plus baisse en 7 jours']
for i in range(10):
    Plus7.append(names_plus[9 - i] +':'+str(dix_plus7d[9-i])+'%')
    Moins7.append(names_min[i] +':'+str(dix_moins7d[i])+'%')
print(json.dumps(Plus7,indent = 4))
print(json.dumps(Moins7,indent = 4))
