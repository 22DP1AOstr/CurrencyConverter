from flask import Flask, render_template, request, redirect, url_for
import requests
import json

# instance of the Flask class
app = Flask(__name__)

# Define a function that converts currency
def convert_currency(amount, from_currency, to_currency):
    api_key = "81b3b6afaff462547ea2c983"    # My API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"   # API request
    response = requests.get(url)    # get request
    data = json.loads(response.text)
    if data["result"] == "error":           
        return f"Error: {data['error-type']}"
    else:
        converted_amount = data["conversion_result"]
        return f"{amount} {from_currency} = {converted_amount} {to_currency}"

# Define a route for the root URL
@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    
    # Check if a POST request was received
    if request.method == "POST":
        # Extract the amount, from_currency, and to_currency values from the form data
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        # Call the convert_currency function to get the conversion result
        result = convert_currency(amount, from_currency, to_currency)
        return render_template("Converter.html", result=result, from_currency=from_currency, to_currency=to_currency)
    else:
        from_currency = 'USD'  # Set a default value for from_currency
        to_currency = 'EUR'
        return render_template("Converter.html", from_currency=from_currency, to_currency=to_currency)

    
# api_key = 'your_api_key_here'
# from_currency = 'USD'
# to_currency = 'EUR'
# amount = 100

# result = convert_currency(api_key, from_currency, to_currency, amount)
# print(result)


# Run the Flask application if this script is run directly
if __name__ == "__main__":
    app.run(debug=True)
