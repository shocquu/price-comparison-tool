from lxml import html
import requests

url = "https://www.x-kom.pl/szukaj?per_page=90&sort_by=accuracy_desc&q=msi%202080"
headers = { "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html" }    
page = requests.get(url, headers)
pageHTML = html.fromstring(page.content)

brands = pageHTML.xpath("//*[@id='listing-container']//div[1]/a/h3/span/text()")
products = pageHTML.xpath("//*[@id='listing-container']//div[1]/a/h3/span/text()")
prices = pageHTML.xpath("//*[@id='listing-container']//div/div/div/div/span[last()]/text()")
test = pageHTML.xpath("//*[@id='listing-container']/div[1]/div/div[2]/div[2]/div[1]/a/h3/span/text()")

#digits = pageHTML.xpath(website["items"]["digits"])
#prices = [i + j for i, j in zip(prices, digits)] 

#for i in range(len(brands)):
#    if brands[i].lower() == input[0].lower().strip():
#        results.append({
#            "brand" : FormatBrand(website["website"], brands[i]),
#            "product" : FormatProduct(website["website"], products[i]),
#            "price" : float(FormatPrice(website["website"], prices[i])),
#            "currency" : website["currency"],
#            "website" : website["website"]
#        })

        

#results = sorted(results, key = lambda k: k["price"])

#for result in results:
#    print("{} {} | {} | {} | {}".format(result["price"], result["currency"], result["website"], result["brand"], result["product"]))