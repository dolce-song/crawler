import requests 
import urllib.robotparser
from bs4 import BeautifulSoup

#url = "https://gihyo.jp/dp"
#url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=130010"
#url = "http://www.jra.go.jp/JRADB/"
#url = "http://www.jra.go.jp"
url = "https://race.netkeiba.com/?pid=race&id=c201903020811&mode=shutuba"

# robots.txtを読んで、クローリングの可否を判断
def confirmation(url):
  robots_url = url + "/robots.txt"
  rp = urllib.robotparser.RobotFileParser()
  rp.set_url(robots_url)
  rp.read()
  if (rp.can_fetch('mybot', robots_url)):
  	print("allowed to crawling " + url)

# firefoxからのアクセスに偽装
headers = {
  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
}
html = requests.get(url, headers=headers)
# テキスト情報から文字コードを推定
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.text, 'html.parser')
print(soup.find_all('span', attrs={'class', 'txt_smaller'}))
