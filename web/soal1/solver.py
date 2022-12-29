import requests
import re
flag = "TCP1P"
r = "http://ctf.tcp1p.com:58161/"

def get_flag(x):
    lines = x.split('\n')
    for line in lines:
        if re.search(r'\b{}\b'.format(flag), line):
            print(line)


r = requests.get(r)
get_flag(r.text)
