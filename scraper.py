import requests
from bs4 import BeautifulSoup
import csv
import os

base_url = "https://results.eci.gov.in/PcResultGenJune2024/Constituencywise"

states = ["U0" + str(u) for u in range(1, 15)] + ["S0" + str(s) if s < 10 else "S" + str(s) for s in range(1, 35)]

results = []

for state in states:
    for constituency_code in range(1, 85):
        constituency_str = str(constituency_code)
        url = f"{base_url}{state}{constituency_str}.htm"
        print("URL", url)
        response = requests.get(url)
        print("Response", response)
        if response.status_code == 404:
            break
        
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')

        table = soup.find('table')  # Find the table element

        # Extract the table headers
        headers = [th.text.strip() for th in table.find_all('th')]

        # Extract the table data
        data = []
        for tr in table.find_all('tr'):
            row = [td.text.strip() for td in tr.find_all('td')]
            if row:
                data.append(row)

        # Write data to CSV file
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)

        print("Headers:", headers)
        print("Data:", data)
        # Extract state name and constituency/district name
        state_name = soup.find('strong').text.strip()
        # constituency_name = soup.find('span').text.strip()

        # Create a folder for each state if it doesn't exist
        state_folder = f"{state_name}"
        if not os.path.exists(state_folder):
            os.makedirs(state_folder)

        # Create a unique filename for each state
        filename = f"{state_name}_{constituency_code}.csv"

        # Write data to CSV file in the state folder
        with open(os.path.join(state_folder, filename), 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)