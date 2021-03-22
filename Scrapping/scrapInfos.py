import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame
import csv
from pprint import pprint

colonnes = ['ville','lien', "Code Insee", "Région", "Département", "Etablissement public de coopération intercommunale (EPCI)",
"Code postal (CP)", "Nom des habitants", "Population (2015)",
"Population : rang national (2015)", "Densité de population (2015)", "Taux de chômage (2015)",
"Pavillon bleu", "Ville d'art et d'histoire", "Ville fleurie", "Ville internet", "Superficie (surface)",
"Altitude min.", "Altitude max.", "Latitude", "Longitude"]

url = "http://www.journaldunet.com/management/ville/aast/ville-64001"

req = requests.get(url)
contenu = req.content
soup = bs(contenu, "html.parser")
dico = {i : "" for i in colonnes}


tables = soup.findAll("table", class_ = "odTable odTableAuto" )

for i in range(len(tables)):
    tousLesTr = tables[i].findAll("tr")
    for tr in tousLesTr[1:]:
        cle = tr.findAll("td")[0].text
        valeur = tr.findAll("td")[1].text

        if "Nom des habitants" in cle:
            dico["Nom des habitants"] = valeur
        else:
            dico[cle] = valeur
pprint(dico)