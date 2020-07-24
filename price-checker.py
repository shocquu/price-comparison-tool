from functions import *
import requests

resp = requests.get("https://api.exchangeratesapi.io/latest?symbols=EUR,PLN")
print(resp.text)

input = input("[Brand Product]: ").split(" ", 1)
websites = GetJSON("websites.json")
products = []

for website in websites:   
    pageHTML = GetPage(website["url"], website["separator"], input)
    itemList = pageHTML.findAll(
        website["itemList"]["tag"], { 
        website["itemList"]["type"] : website["itemList"]["title"]
    })
    
    for item in itemList:
        brandName = item.findAll(
            website["brandItem"]["tag"], {
            website["brandItem"]["type"] : website["brandItem"]["title"]
        })[0].text    
        brandName = FormatBrand(website["website"], brandName)
    
        if brandName.lower() == input[0].lower().strip():
            productName = item.findAll(
                website["productItem"]["tag"], {
                website["productItem"]["type"] : website["productItem"]["title"]
            })[0].text
            productName = FormatProduct(website["website"], productName)
        
            currentPrice = item.findAll(
                website["priceItem"]["tag"], {
                website["priceItem"]["type"] : website["priceItem"]["title"]
            })[0].text
            currentPrice = FormatPrice(website["website"], currentPrice)
            
            products.append({
                "brand" : brandName,
                "product" : productName,
                "price" : float(currentPrice),
                "currency" : website["currency"],
                "website" : website["website"]
            })

products = sorted(products, key = lambda k: k["price"])

for product in products:
    print("{} {} | {} | {} | {}".format(product["price"], product["currency"], product["website"], product["brand"], product["product"]))
