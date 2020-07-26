from lxml import html
import requests
import json

def GetURL(url, separator, input):
    url += input[0].replace(" ", separator) + separator + input[1].replace(" ", separator)
    return url

def GetPage(url):   
    headers = { "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html" }
    page = requests.get(url, headers)
    return html.fromstring(page.content)

def GetJSON(path):
    with open(path) as data:
        return json.load(data)

def LookForKeywords(keywords, product):         
    true = 1

    for keyword in keywords:
        if keyword in product.lower():
            true = true * 1
        else:
            true = 0
    return true    

def DisplayResults(results, limit):
    results = sorted(results, key = lambda k: k["price"])
    limit = len(results) if limit == 0 else limit

    for i in range(limit):    
        print("{} {} | {} | {} | {}".format(results[i]["price"], results[i]["currency"], results[i]["website"], results[i]["brand"], results[i]["product"]))

def FormatBrand(website, brandName):
    if brandName[0].isdigit():
        brandName = brandName.split(" ", 1)[1]

    if website == "Caseking" :
        return brandName.strip().split(" ")[0]
    elif website == "MindFactory":
        return brandName.split(" ")[0]
    elif website == "Alternate":
        return brandName.split(" ")[0]
    elif website == "x-kom":
        return brandName.strip().split(" ", 1)[0]        

def FormatProduct(website, productName):
    if website == "Caseking":
        return productName.strip().replace(",", "")
    elif website == "MindFactory":
        return productName.split(" ", 1)[1]
    elif website == "Alternate":
        return productName.rsplit(" ", 1)[0]
    elif website == "x-kom":
        return productName.split(" ", 1)[1]

def FormatPrice(website, currentPrice):
    if website == "Caseking":
        return currentPrice.strip().replace(u"\u20AC*", "").replace(".", "").replace(",", ".")
    elif website == "MindFactory":
        return currentPrice.strip().strip().replace(" ", "").replace("*", "").replace(".", "").replace(",", ".")
    elif website == "Alternate":
        return currentPrice.replace(u"\u20AC ", "").replace(".", "").replace(",", ".").replace("-", "00").replace("*", "")
    elif website == "x-kom":
        return currentPrice.strip().rsplit(" ", 1)[0].replace(" ", "").replace(",", ".")
