import requests
from bs4 import BeautifulSoup
import csv
import os


url="https://results.eci.gov.in/PcResultGenJune2024/index.htm"
response = requests.get(url)
# print(response)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')
table = soup.find('table')
headers = [th.text.strip() for th in table.find_all('th')]
# print(headers)
data = []
for tr in table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    if row:
        data.append(row)
with open('outputparty.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)