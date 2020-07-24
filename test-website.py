from urllib.request import urlopen as req
from bs4 import BeautifulSoup as bsoup

from lxml import html
import requests

page = requests.get('https://www.alternate.de/html/search.html?query=rx+580&x=0&y=0')
tree = html.fromstring(page.content)
print(tree)

#url = "https://www.mindfactory.de/search_result.php?select_search=0&search_query=amd+ryzen"
#client = req(url)
#page_html = client.read()
#client.close()
#page_html = bsoup(page_html, "html.parser")

#page_html = bsoup(html, "html.parser")
#items = page_html.findAll("div", {"class" : "p"})

#for item in items:
    #brandName = item.findAll("div", {"class" : "pname"})[0].text.split(" ")[0]
    #print(brandName)
    #productName = item.findAll("div", {"class" : "pname"})[0].text.split(" ", 1)[1]
    #print(productName)
    #currentPrice = item.findAll("div", {"class" : "pprice"})[0].text.replace(" €\xa0", "").replace("*", "").replace(",", ".")
    #currentPrice = item.findAll("div", {"class" : "pprice"})[0].text.strip().strip().replace("€\xa0", "").replace("*", "").replace(".", "").replace(",", ".")
    #print(currentPrice)

    #print("{} | {} | {}".format(currentPrice, brandName, productName,)) 
        