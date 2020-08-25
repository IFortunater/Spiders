import requests
from lxml import etree

ip_list = []
url = "http://www.goubanjia.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
trs = html.xpath('//tbody/tr')
for tr in trs:
    ip = ''.join(tr.xpath('td[1]/*[contains(@style,"display")]/text()'))
    port = tr.xpath('td[1]/span[@class="port CEAAA"]/text()')
    is_high = (tr.xpath('td[2]/a/text()')[0] == '高匿')
    if port != []:
        port = 3000
    else:
        port = 9999
    print(ip+":"+str(port), is_high)
    # ip_list.append(ip)

