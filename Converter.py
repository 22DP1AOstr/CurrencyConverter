import requests
import json

def convert_currency(amount, from_currency, to_currency):
    api_key = "81b3b6afaff462547ea2c983" # My API key 
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = json.loads(response.text)
    if data["result"] == "error":
        return f"Error: {data['error-type']}"
    else:
        converted_amount = data["conversion_result"]
        return f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"     # Atgriež konvertēto valūtu

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

result = convert_currency(amount, from_currency, to_currency)
print(result)
