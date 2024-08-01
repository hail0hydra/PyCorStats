import requests
import time
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

url = "https://www.worldometers.info/coronavirus/#countries"
response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', id='main_table_countries_today')

if table:
    rows = table.find_all('tr')
    data = [['Country / Continent','Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 'Serious, Critical', 'Top Cases / 1M pop', 'Deaths / 1M pop', 'Total Tests', 'Tests / 1M pop', 'Population']]
    data.append(data[0])

    for index, row in enumerate(rows[1:51], start=1):
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols[1:15])

    df = pd.DataFrame(data[1:], columns=data[0])

    print(tabulate( df, tablefmt="fancy_grid"))
    # print(data)
    

else:
    print("Table not found.")

time.sleep(5)

input("Press Enter to exit...")

