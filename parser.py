

from bs4 import BeautifulSoup as BS
import requests
import pandas as PD
file= "auto.csv"
url = "https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&fuel.id[0]=5&abroad.not=0&custom.not=1&size=20"
def car(sitle=url):

    rq=requests.get(url)
    if  rq.status_code==200:
        txt = BS(rq.text, features="html.parser")
        pars=txt.find_all("span", {"data-currency":"USD"})
        auto=[]
        s=0
        for i in pars:
            s=s+1
            auto.append(i.text)
        # res=pars[0].find("span")
        # print(res)
        print("audi ",auto[0])
        print("volkswagen ", auto[1])
        print("mersrdes ", auto[2])
        print("\n")
        costAuto=[]
        for i in pars:
            costAuto.append(i.text)
        autoName=[" Audi A6 2018 "," Volkswagen Golf 2016 "," Volvo XC90 2021 "," Ford Fusion 2019 "," Toyota RAV4 2019 "]
        for i in range(5):
            print(autoName[i],"==",costAuto[i])

if car()==True:
    print("soxraneno")
else:
    print("error")

f = PD.DataFrame(data=car())
f.to_csv(file)