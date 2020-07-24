from urllib.request import urlopen as request
from bs4 import BeautifulSoup as bsoup
import json

def GetPage(url, separator, brandInput, nameInput):    
    url += brandInput.replace(" ", separator) + nameInput.replace(" ", separator)
    client = request(url)
    pageHTML = client.read()
    client.close()
    return bsoup(pageHTML, "html.parser")

def GetJSON(path):
    with open(path) as data:
        return json.load(data)

def FormatBrand(website, brandName):
    if website == "Caseking" :
        return brandName.strip()
    elif website == "x-kom":
        return brandName.strip().split(" ", 1)[0]        

def FormatProduct(website, productName):
    if website == "Caseking":
        return productName.strip().replace(",", "")
    elif website == "x-kom":
        return productName.split(" ", 1)[1]

def FormatPrice(website, currentPrice):
    if website == "Caseking":
        return currentPrice.strip().replace(u"\u20AC*", "").replace(".", "").replace(",", ".")
    elif website == "x-kom":
        return currentPrice.strip().rsplit(" ", 1)[0].replace(" ", "").replace(",", ".")