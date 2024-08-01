import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://www.worldometers.info/coronavirus/#countries"
response = requests.get(url)
html_content = response.content

headers = ['Country','Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 'Serious, Critical', 'Top Cases / 1M pop', 'Deaths / 1M pop', 'Total Tests', 'Tests / 1M pop', 'Population']

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', id='main_table_countries_today')

if table:
    rows = table.find_all('tr')

    for index, row in enumerate(rows[1:], start=1):
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if cols[0] == '2': 
            table_data = [headers] + [cols[1:15]] 
            print(tabulate(table_data, tablefmt="fancy_grid"))
else:
    print("Table not found.")
