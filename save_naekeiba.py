import requests
import os

#url = "https://race.netkeiba.com/abroad/?pid=race&id=c2019A0072704&mode=shutuba"
url = "https://race.netkeiba.com/?pid=race&id=c201904020211&mode=shutuba"

res = requests.get(url)
res.encoding = res.apparent_encoding

path = os.getcwd()
keiba_data = path + "/netkeiba_g3_nigata_0728.html"

f = open(keiba_data, mode='w')
f.write(res.text)
f.close()
