import requests
import re
import random


# trả không thèm
def genproxy():
    # rồ xi gan ra nơ ton
    url = 'https://free-proxy-list.net/anonymous-proxy.html'
    response = requests.get(url)
    content = response.text
    proxymath = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})')
    matches = proxymath.findall(content)
    return matches