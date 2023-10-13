# import requests
# from bs4 import BeautifulSoup
#
# url = "https://minfin.com.ua/currency/"
# rq = requests.get(url)
# soup = BeautifulSoup(rq.text, "html.parser")
#
# dollar_rates = []
# for div in soup.find_all("div", class_="sc-1x32wa2-9 bKmKjX"):
#     dollar_rate = div.text
#     dollar_rates.append(dollar_rate)
#
# usd1='.'.join(dollar_rates.split(',')[:-1])
#
# print(usd1)
# grn=int(input("enter you grivnya: "))
# print("Курс долара: "+dollar_rates[0])
# usd=grn*int(dollar_rates[0])
# print("ваши долары: "+usd)

import requests
from bs4 import BeautifulSoup

url = "https://minfin.com.ua/currency/"
rq = requests.get(url)
soup = BeautifulSoup(rq.text, "html.parser")

dollar_rates = []
for div in soup.find_all("div", class_="sc-1x32wa2-9 bKmKjX"):
    dollar_rate = div.text
    dollar_rates.append(dollar_rate)

if dollar_rates:
    rate = dollar_rates[0][:2]
    grn = int(input("Введите ваши гривны: "))
    print("Курс доллара: " + rate)
    print("Ваши долари: ",grn / int(rate))
else:
    print("Курс доллара не найден")
