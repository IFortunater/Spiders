import requests
from lxml import etree
from BasicKnowledge.测试代理池 import TestIPPool

page = 1
url = "http://www.glidedsky.com/level/web/crawler-ip-block-%d" % page
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
proxys = []


pool = TestIPPool()
pool.make_ip_pool()
for proxy in pool.ip_pool:
    proxy = proxy.strip()
    proxys.append(proxy)
for proxy in proxys:
    try:
        proxies = {
            'http': 'http://' + proxy,
            'https':'https://' + proxy
        }
        response = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
        html = etree.HTML(response.text)
        res = html.xpath('//div[@class="row"]/div/text()')
        res = [x.strip() for x in res]
        if res:
            print(res)
            page += 1
    except:
        pass