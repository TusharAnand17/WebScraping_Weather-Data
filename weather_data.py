import requests
from bs4 import BeautifulSoup
import requests_html

city = input("Enter the City name: ")
try:
    url = f'https://www.google.com/search?q=weather+{city}'
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, "html.parser")
    temp = (soup.select('span#wob_tm')[0].get_text())
    unit = soup.select('div.vk_bk.wob-unit span.wob_t')[0].get_text()
    pp = soup.select('div.wtsRwe span#wob_pp')[0].get_text()
    hm = soup.select('div.wtsRwe span#wob_hm')[0].get_text()
    wind = soup.select('div.wtsRwe span#wob_ws')[0].get_text()  
    weather = soup.select('div#wob_dcp span#wob_dc')[0].get_text()

    print("\n\n==========================================\n")
    print("City:",city)
    print(f"Temperature: {temp}{unit}")
    print("Precipitation:",pp)
    print("Humidity:",hm)
    print("Wind:",wind)
    print("Weather is",weather)
    print("\n==========================================\n")

except Exception as e:
    print("\nMake sure You have good internet connection and city you entered is correct\nTry Again....")