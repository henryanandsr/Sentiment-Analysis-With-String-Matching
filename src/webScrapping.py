import requests
from bs4 import BeautifulSoup

url = "https://www.thejakartapost.com/business/economy?page="

list_judul = []

for i in range(1,50):
    response = requests.get(url+str(i))

    soup = BeautifulSoup(response.text, "html.parser")

    judul_h2 = soup.find_all("h2")

    for judul in judul_h2:
        list_judul.append(judul.text)

    for el in list_judul:
        print(el)
with open("list_judul.txt", "w") as file:
    for judul in list_judul:
        cleaned_judul = judul.strip()
        file.write(cleaned_judul + "\n")
