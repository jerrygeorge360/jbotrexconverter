from currencyconverter import countriespair
import requests
data=requests.get()


def letlook(value=[]):
    from currencyconverter import Location,Nominatim
    try:
        geolocator=Nominatim(user_agent='locate')
        latitude=value[0]
        longitude=value[1]
        location=geolocator.geocode(latitude+","+longitude)
        raw_location=location.raw
        address=raw_location['display_name']
        address1=address.split(',')
        address2=str(address1[-1])
        currency2=countriespair.countries.get(address2)
    except:
        currency2 = countriespair.countries.get('Nigeria')

    return currency2


def api(currency='USD', regional='GBP', amount=''):
    url = "https://just-currencies.p.rapidapi.com/convert"

    querystring = {"amount": amount, "from": currency, "to": regional, "date": "2006-05-05"}

    headers = {
        'x-rapidapi-host': "just-currencies.p.rapidapi.com",
        'x-rapidapi-key': "631edcacf0msh95abea4bcffab6ap102821jsnd0b2d0c2beaa"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = response.json()
    my_converted_money = round(float(response_json.get('result')['request']),2)

    print(f' hello {regional}')
    print(response.json())
    return my_converted_money

