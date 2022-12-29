import requests
import re
flag = "TCP1P"
url = "http://ctf.tcp1p.com:45659/"

def get_flag(x):
    lines = x.split('\n')
    for line in lines:
        if re.search(r'\b{}\b'.format(flag), line):
                f = line
                break
    return f
# print(md5(240610708) == md5(QNKCDZO)) => True
r = requests.get(url, params={'secret' : 'QNKCDZO'})
print(get_flag(r.text))