from urllib.request import urlopen as request
from bs4 import BeautifulSoup as bsoup

input = input("[Brand, Product]: ")
brandInput, nameInput = input.split(", ")
products = []

# X-KOM
url = "https://www.x-kom.pl/szukaj?q=" + brandInput.replace(" ", "%20") + nameInput.replace(" ", "%20")
client = request(url)
page_html = client.read()
client.close()
page_html = bsoup(page_html, "html.parser")

items = page_html.findAll("div", {"class" : "sc-162ysh3-1 cVKkKd sc-bwzfXH dXCVXY"})

for item in items:
    brandName = item.findAll("h3", {"class" : "sc-1yu46qn-12 edAUTq sc-16zrtke-0 hovdBk"})[0].text.strip().split(" ", 1)[0]
     
    if(brandName.lower() == brandInput.lower()):
        productName = item.findAll("h3", {"class" : "sc-1yu46qn-12 edAUTq sc-16zrtke-0 hovdBk"})[0].text.split(" ", 1)[1]
        currentPrice = item.findAll("span", {"class" : "sc-6n68ef-0 sc-6n68ef-3 iertXt"})[0].text.strip().rsplit(" ", 1)[0].replace(" ", "").replace(",", ".")
    
        products.append({
            "brand" : brandName,
            "product" : productName,
            "price" : float(currentPrice),
            "website" : "x-kom"
        })

# Display products sorted by price in ascending order
for product in products:
    print("Product: " + str(product["price"]) + " | " + product["brand"] + " | " + product["product"])    