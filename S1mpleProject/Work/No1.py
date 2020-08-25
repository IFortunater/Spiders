import requests
from lxml import etree
from bs4 import BeautifulSoup
url = "https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.status_code)
page_text = response.text
html = etree.HTML(page_text)
res = html.xpath('//tr[@class="alt"]/text()')
print(res)
# soup = BeautifulSoup(page_text)
# print(soup.prettify())

