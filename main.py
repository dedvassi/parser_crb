import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)
xml = response.content
soup = BeautifulSoup(xml, "lxml-xml")

currency_ids = {
    "USD": "R01235",
    "EUR": "R01239",
    "CNY": "R01375"
}
for name, cur_id in currency_ids.items():
    valute = soup.find("Valute", attrs={"ID": cur_id})
    value = valute.find("Value").text
    print(f"{name}: {value} руб.")