import requests
from lxml import etree

ip_list = []
url = "https://www.kuaidaili.com/free/inha/1/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
trs = html.xpath('//tbody/tr')
for tr in trs:
    ip = tr.xpath('td[1]/text()')[0] + ":" +tr.xpath('td[2]/text()')[0]
    is_high = (tr.xpath('td[3]/text()')[0] == '高匿名')
    print(ip, is_high)

