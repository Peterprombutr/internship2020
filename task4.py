from bs4 import BeautifulSoup
import requests
import flask
from flask import request, jsonify
from collections import defaultdict 
from operator import itemgetter 
from itertools import groupby 

url = "http://theinternship.io/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html

logo_url = soup.findAll("img", "center-logos")
companies_url = soup.findAll("span", "list-company")

company_dict = {}

for index in range(len(logo_url)):
    company_dict[logo_url[index]['src']] = companies_url[index].get_text()

# print(company_dict)

sorted_company_dict = sorted(company_dict.items(), key=lambda x: x[0])
companies_api =[]
for company in sorted_company_dict:
    print(company[0])
    company = {"logo": str(url) + company[0]}
    companies_api.append(company)

################################################################

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Driver code 
# print(companies_api) 

@app.route("/companies", methods=["GET"])
def api_all():
    return jsonify({"companies": companies_api})

app.run()

