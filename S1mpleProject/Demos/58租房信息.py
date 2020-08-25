import time
import requests
from lxml import etree
# 代理服务器
proxy_host = 'proxy.abuyun.com'
proxy_port = '9020'

# 代理隧道验证信息
proxy_user = 'H8U61RTM72Q1J85D'
proxy_pass = 'B83C3EF0F8E8B0A2'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass,
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta,
}

cityNames = ['chaoyang','haidian', 'fengtai', 'daxing', 'tongzhouqu',
             'fangshan', 'shunyi', 'xicheng','dongcheng', 'miyun', 'shijingshan',
             'huairou', 'mentougou', 'yanqing', 'pinggu']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}
# allCityInfoDict = {}
for cityName in cityNames:
    # cityInfoDict = {}
    url = "https://bj.58.com/{}/chuzu/".format(cityName)
    response = requests.get(url, headers=headers, proxies=proxies)
    while url != response.url:
        print(response.url)
        response = requests.get(url, headers=headers)
    print(response.url, response.status_code)
    html = etree.HTML(response.text)
    zuFanlis = html.xpath('//ul[@class="house-list"]/li')
    for li in zuFanlis:
        try:
            address = ",".join(li.xpath('div[2]/p[@class="infor"]/a/text()'))
            OtherInfo = li.xpath('div[2]/h2/a[1]/text()')[0].strip()
            money = li.xpath('div[3]/div[@class="money"]/b/text()')[0] + li.xpath('div[3]/div[@class="money"]/text()')[1].strip()
            print(address)
            print(OtherInfo)
            print(money)
            print()
        except:
            pass
    time.sleep(2)
