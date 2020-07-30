import requests
import requests_cache

requests_cache.install_cache("./data/cached-currencies", expire_after = 1800)
api_url = "https://api.exchangeratesapi.io/latest"
requests_cache.remove_expired_responses()
data = requests.get(api_url).json()
rates = data["rates"]

def Validate(currency):
    if currency.upper() == "EUR":
        return True
    else:
        for each in rates:
            if currency == each:
                return True
            
        return False

def Convert(from_currency, to_currency, amount_in_eur):
    if Validate(to_currency) == False:
        to_currency = "USD"

    if to_currency == "EUR":
        return amount_in_eur

    if from_currency.upper() != "EUR":
        amount_in_eur /= rates[from_currency.upper()]
            
    return round(rates[to_currency.upper()] * amount_in_eur, 2)