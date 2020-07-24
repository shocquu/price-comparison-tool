from functions import *

input = input("[Brand, Product]: ")
brandInput, nameInput = input.split(", ")
websites = GetJSON("websites.json")
products = []

for website in websites:
    pageHTML = GetPage(website["url"], website["separator"], brandInput, nameInput)
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
    
        if brandName.lower() == brandInput.lower().strip():
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
    print("Product: %.2f %s | %s | %s | %s" % (product["price"], product["currency"], product["website"], product["brand"], product["product"]))
