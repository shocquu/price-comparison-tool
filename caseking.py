# CASEKING
url = "https://www.caseking.de/search?sSearch=" + brandInput.replace(" ", "+") + nameInput.replace(" ", "+")
client = request(url)
page_html = client.read()
client.close()
page_html = bsoup(page_html, "html.parser")

items = page_html.findAll("div", {"class" : "artbox grid_5 last"})

# Add products to a list
for item in items:
    brandName = item.findAll("span", {"class" : "ProductSubTitle"})[0].text.strip() 

    if(brandName.lower() == brandInput.lower()):
        productName = item.findAll("span", {"class" : "ProductTitle"})[0].text.strip().replace(",", "") 
        currentPrice = item.findAll("span", {"class" : "price"})[0].text.strip().replace(u"\u20AC*", "").replace(".", "").replace(",", ".")
        
        products.append({
            "brand" : brandName,
            "product" : productName,
            "price" : float(currentPrice),
            "website" : "caseking"
        })
  
products = sorted(products, key=lambda k: k["price"])