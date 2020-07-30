import modules.functions as func
import modules.currency_converter as cc
import argparse

_currency = "USD"
_limit = 0

def CrawlForData(keywords, limit):    
    websites = func.GetJSON("data/websites-data.json")
    maker = keywords[0].lower().strip()
    specs = keywords[1].lower().split(" ")
    results = []    

    for website in websites:
        url =  func.GetURL(website["url"], website["separator"], keywords)
        pageHTML = func.GetPage(url)

        brands = pageHTML.xpath(website["items"]["brands"])
        products = pageHTML.xpath(website["items"]["products"])
        prices = pageHTML.xpath(website["items"]["prices"])

        for i in range(len(brands)):
            brand = func.FormatBrand(website["website"], brands[i])
            
            if brand.lower() in maker: 
                product = func.FormatProduct(website["website"], products[i])

                if func.LookForKeywords(specs, product):
                    price = float(func.FormatPrice(website["website"], prices[i]))
                    price = cc.Convert(website["currency"], _currency, price)
                    
                    results.append({
                        "brand"     : brand,
                        "product"   : product,
                        "price"     : price,
                        "currency"  : _currency,
                        "website"   : website["website"]
                    })

    if limit == 0 or limit > len(results):
        limit = len(results)

    results = func.SortByPrice(results)
    
    return results[:limit]

def UseCrawler():
    keywords = input("[Brand Product]: ").split(" ", 1)
    results = CrawlForData(keywords, _limit)
    func.DisplayResults(results)

def UseShoppingList():    
    with open("shopping-list.txt", "r") as file:
        shoppingList = file.readlines()
    
    shoppingList = [x.strip() for x in shoppingList]
    results = []   
    total = 0

    for item in shoppingList: 
        line = item.split(",")
        quantity = int(line[1].strip())
        keywords = line[0].split(" ", 1)
        result = {}

        if CrawlForData(keywords, 1):
            result = CrawlForData(keywords, 1)[0]
            result["qty"] = quantity
            total += result["price"] * quantity
        else:
            result["price"] = 0
            result["currency"] = _currency
            result["qty"] = quantity
            result["brand"] = keywords[0].capitalize()
            result["product"] = keywords[1].capitalize()
            result["website"] = "-"

        results.append(result)
    
    func.DisplayCart(results, total)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", type=int, nargs="+", help="set how many records you want to be displayed")
    parser.add_argument("-c", "--currency", action="store", help="set currency")
    parser.add_argument("-s", "--list", dest="accumulate", action="store_true", help="use shopping list")
    args = parser.parse_args()

    if args.limit != None:
        _limit = args.limit[0]
    if args.currency != None and cc.Validate(args.currency.upper()):
        _currency = args.currency.upper() 
    if args.accumulate:
        UseShoppingList()
    else:
        UseCrawler()