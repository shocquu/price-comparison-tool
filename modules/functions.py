from lxml import html
import requests
import requests_cache
import json

def GetURL(url, separator, input):    
    url = url.format(input[0].replace(" ", separator), separator, input[1].replace(" ", separator))
    return url

def GetPage(url):   
    headers = { "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html" }
    requests_cache.install_cache("./data/cached-results", expire_after = 3600)
    requests_cache.remove_expired_responses() 
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

def SortByPrice(results):
    results = sorted(results, key = lambda k: k["price"])
    return results

def GetTemplate():
    header = f'| {"PRICE":14} | {"WEBSITE":14} | {"BRAND":12} | {"PRODUCT NAME":70} |'
    border = "+----------------+----------------+--------------+------------------------------------------------------------------------+"
    return header, border

def DisplayResults(results):    
    if len(results) > 0:
        header, border= GetTemplate()        

        print(border)
        print(header)
        print(border)
        
        for i in range(len(results)):
            print(f'| {results[i]["price"]:>7.2f} {results[i]["currency"]:<6} | {results[i]["website"]:14} | {results[i]["brand"]:<12} | {results[i]["product"]:<70} |')
           
        print(border)        
    else:
        print("No results matching your criteria.")

def DisplayCart(results, total):
    if len(results) > 0:        
        header, border= GetTemplate()
        header = header[:16] + f' | {"QTY":3} ' + header[16:51] + f'{"PRODUCT NAME":63} |'
        border = border[:24] + "+------" + border[24:50] + border[57:]

        print(border)
        print(header)
        print(border)

        for i in range(len(results)):            
            print(f'| {results[i]["price"]:>7.2f} {results[i]["currency"]:<6} | {results[i]["qty"]:<4} | {results[i]["website"]:14} | {results[i]["brand"]:<12} | {results[i]["product"]:<63} |')

        print(border)
        print(f'| {"TOTAL:":>107} {total:>7.2f} {results[0]["currency"]:>3} |')
        print("+-------------------------------------------------------------------------------------------------------------------------+")
    else:
        print("It look like your cart is empty.")

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