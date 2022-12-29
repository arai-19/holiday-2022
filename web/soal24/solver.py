import requests

url = "http://challenge01.root-me.org/web-serveur/ch2/"

r = requests.get("http://challenge01.root-me.org/web-serveur/ch2/", headers={'user-agent':'admin'})
print(r.text, r.headers)