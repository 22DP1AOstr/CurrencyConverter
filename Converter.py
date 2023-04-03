from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

def convert_currency(amount, from_currency, to_currency):
    api_key = "81b3b6afaff462547ea2c983" # My API key 
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = json.loads(response.text)
    if data["result"] == "error":
        return f"Error: {data['error-type']}"
    else:
        converted_amount = data["conversion_result"]
        return f"{amount} {from_currency} = {converted_amount} {to_currency}"
    

@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        result = convert_currency(amount, from_currency, to_currency)
        return render_template("Converter.html", result=result)
    else:
        return render_template("Converter.html")
    

# api_key = 'your_api_key_here'
# from_currency = 'USD'
# to_currency = 'EUR'
# amount = 100

# result = convert_currency(api_key, from_currency, to_currency, amount)
# print(result)

if __name__ == "__main__":
    app.run(debug=True)
    
