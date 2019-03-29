#verkefni2_6
import json
from urllib.request import urlopen

def count_names(start):
    get_url = urlopen('https://hagstofa.is/media/49531/names.json')
    get_json = json.loads(get_url.read())
    names = []
    first = 0
    second = 0
    len_of_start = len(start)
    for item in get_json:
        names.append(item)
    for name in names:
        if start in name['Nafn'][0:len_of_start]: #comparing substring start to any names in the list
            first += int(name['Fjoldi1'])
            second += int(name['Fjoldi2'])

    return (first, second)

count_names('Bja')
#(3312, 1555)
count_names('Wat')
#(8, 2)
count_names('Snati')
#(0, 0)

"""
import json
from urllib.request import urlopen


r = urlopen('https://hagstofa.is/media/49531/names.json')
r.read()

import requests
import json
import urllib

url="https://hagstofa.is/media/49531/names.json"
r=requests.get(url)
t=json.loads(r.content)
for i in range(len(t)):
"""

response = urlopen("http://mbl.is")
data1 = response.read()
data2 = response.read()

n1 = len(data1)
n2 = len(data2)
