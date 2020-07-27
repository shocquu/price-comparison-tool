from lxml import html
import requests
import requests_cache
import json

def GetURL(url, separator, input):
    #url += input[0].replace(" ", separator) + separator + input[1].replace(" ", separator)
    url = url.format(input[0].replace(" ", separator), separator, input[1].replace(" ", separator))
    return url

def GetPage(url):   
    headers = { "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html" }
    requests_cache.install_cache("./data/cached-results", expire_after = 3600)
    page = requests.get(url, headers)
    return html.fromstring(page.content)

def GetJSON(path):
    with open(path) as data:
        return json.load(data)

def LookForKeywords(keywords, product):
    isMatching = True

    for keyword in keywords:        
        if keyword not in product.lower():
            isMatching = False
    return isMatching         

def DisplayResults(results, limit):
    results = sorted(results, key = lambda k: k["price"])
    limit = len(results) if limit == 0 else limit

    if len(results) > 0:
        print("\n+-------------------+----------------+--------------+----------------------------------------------------------------------------------+")       
        print(f'| {"   PRICE":17} | {"WEBSITE":14} | {"BRAND":12} | {"PRODUCT NAME":80} |')
        print("+-------------------+----------------+--------------+----------------------------------------------------------------------------------+")

        for i in range(limit):            
            print(f'| {results[i]["price"]:>10.2f} {results[i]["currency"]:<6} | {results[i]["website"]:14} | {results[i]["brand"]:<12} | {results[i]["product"]:<80} |')
        
        print("+-------------------+----------------+--------------+----------------------------------------------------------------------------------+\n")
    else:
        print("Sorry, we couldn't find any results.")

def IsDigit(name):
    if name[0].isdigit():
        number = name.split(" ", 1)[0]        
        return name.split(" ", 1)[1] + " " + number
    else:
        return name

def FormatBrand(website, brandName):
    brandName = IsDigit(brandName)
        
    if website == "Caseking" :
        return brandName.strip().split(" ")[0]
    elif website == "MindFactory":
        return brandName.split(" ")[0]
    elif website == "Alternate":
        return brandName.split(" ")[0]
    elif website == "x-kom":
        return brandName.strip().split(" ", 1)[0]        

def FormatProduct(website, productName):
    productName = IsDigit(productName)

    if website == "Caseking":
        return productName.strip().replace("-...", "")
    elif website == "MindFactory":
        return productName.split(" ", 1)[1]
    elif website == "Alternate":
        return productName.rsplit(", ", 1)[0]
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
