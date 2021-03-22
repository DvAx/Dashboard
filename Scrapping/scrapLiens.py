import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame
import csv
#bloc size1of2 odSquareList

colonnes = ["ville", "lien"]

#Creation de notre tableau
tableau = DataFrame(columns = colonnes)
tableau.to_csv("dataset\\liensVilles.csv", index = False)

dico = {}
dico["ville"] = ""
dico["lien"] = ""

url = "http://www.journaldunet.com/management/ville/index/villes?page="


with open("dataset\\liensVilles.csv", "a", encoding="utf-8") as cvsfile:
    writer = csv.DictWriter(cvsfile, fieldnames=colonnes, lineterminator = "\n")
    for numeroPage in range(1,701):
        print(numeroPage)
        req = requests.get(url + str(numeroPage))
        contenu = req.content
        soup = bs(contenu,"html.parser")

        tousLesLiens = soup.findAll("a")

        for lien in tousLesLiens:
            if "/ville-" in lien["href"]:
                dico["lien"] = lien["href"]
                dico["ville"] = lien.text

                writer.writerow(dico)


