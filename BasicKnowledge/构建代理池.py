import time
import requests
from lxml import etree


class IPPool:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    IP_list = []

    def crwal_page1(self):
        for i in range(1, 31):
            try:
                url = "https://ip.jiangxianli.com/?page=%d" % i
                print(url)
                response = requests.get(url, headers=self.headers)
                page_text = response.text
                html = etree.HTML(page_text)
                trs = html.xpath('//tbody/tr')
                for tr in trs:
                    infoList = tr.xpath('td/text()')
                    if infoList[2] == '高匿':
                        self.IP_list.append(infoList[0] + ":" + infoList[1])
                        print(infoList[0] + ":" + infoList[1])
                time.sleep(2)
            except:
                print("获取失败")

    def crwal_page2(self):
        try:
            url = "http://www.goubanjia.com/"
            print(url)
            response = requests.get(url, headers=self.headers)
            html = etree.HTML(response.text)
            trs = html.xpath('//tbody/tr')
            for tr in trs:
                ip = ''.join(tr.xpath('td[1]/*[contains(@style,"display")]/text()'))
                port = tr.xpath('td[1]/span[@class="port CEAAA"]/text()')
                is_high = (tr.xpath('td[2]/a/text()')[0] == '高匿')
                ip = ip + ":" + str(port)
                if is_high:
                    print(ip)
                    self.IP_list.append(ip)
        except:
            print("获取失败")

    def crwal_page3(self):
        for i in range(1, 31):
            try:
                url = "https://www.kuaidaili.com/free/inha/%d/" % i
                print(url)
                response = requests.get(url, headers=self.headers)
                html = etree.HTML(response.text)
                trs = html.xpath('//tbody/tr')
                for tr in trs:
                    ip = tr.xpath('td[1]/text()')[0] + ":" + tr.xpath('td[2]/text()')[0]
                    is_high = (tr.xpath('td[3]/text()')[0] == '高匿名')
                    if is_high:
                        self.IP_list.append(ip)
                        print(ip)
                time.sleep(2)
            except:
                print("获取失败")

    def writeToFile(self):
        fp = open('IP_Pool.txt', 'w', encoding='utf-8', newline='')
        for ip in self.IP_list:
            fp.write(ip + '\n')
        fp.close()

    def make_Pool(self):
        self.crwal_page1()
        self.crwal_page2()
        self.crwal_page3()
        self.writeToFile()


if __name__ == '__main__':
    p = IPPool()
    p.make_Pool()