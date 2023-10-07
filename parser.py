import requests
url="https://coinmarketcap.com/"
rq=requests.get(url)
text_rq=rq.text
pars=text_rq.split("<span>")
coin=[]
for tag in pars:
    if tag.startswith("$"):
        for t in tag.split("</span>"):
            if t.startswith("$") and t[1].isdigit():
                coin.append(t)


print("Bitkoin "+coin[0])
print("Etherium "+coin[1])
print("USDT "+coin[2])
