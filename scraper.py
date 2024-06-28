import requests

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