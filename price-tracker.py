from modules.functions import *

input = input("[Brand Product]: ").split(" ", 1)
websites = GetJSON("data/websites-data.json")
keywords = input[1].lower().split(" ")
results = []
limit = 0

for website in websites:
    url =  GetURL(website["url"], website["separator"], input)    
    pageHTML = GetPage(url)

    brands = pageHTML.xpath(website["items"]["brands"])
    products = pageHTML.xpath(website["items"]["products"])
    prices = pageHTML.xpath(website["items"]["prices"])
    #decimals = pageHTML.xpath(website["items"]["decimals"])
    #prices = [i + j for i, j in zip(prices, decimals)]
    
    for i in range(len(brands)):
        brand = FormatBrand(website["website"], brands[i])
        
        if brand.lower() in input[0].lower().strip(): 
            product = FormatProduct(website["website"], products[i])            

            if LookForKeywords(keywords, product):
                price = FormatPrice(website["website"], prices[i])
                
                results.append({
                    "brand"     : brand,
                    "product"   : product,
                    "price"     : float(price),         
                    "currency"  : website["currency"],
                    "website"   : website["website"]
                })

DisplayResults(results, limit)