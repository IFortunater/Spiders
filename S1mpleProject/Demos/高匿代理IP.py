import csv
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
IP_list = []
def crwal_page(url):
    response = requests.get(url, headers=headers)
    page_text = response.text
    html = etree.HTML(page_text)
    trs = html.xpath('//tbody/tr')
    for tr in trs:
        infoList = tr.xpath('td/text()')
        if infoList[2] == '高匿':
            IP_list.append(infoList)


def writeToFile():
    fp =  open('../DemoFiles/HighIP.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(fp)
    FirstLine = ['IP', 'Port', 'Position', 'Speed', 'LiveTime', 'LastTestTime']
    writer.writerow(FirstLine)
    for List in IP_list:
        print(List)
        try:
            writer.writerow([List[0], List[1], List[4], List[6], List[7], List[8]])
        except:
            pass
    fp.close()


if __name__ == '__main__':
    for i in range(1, 11):
        base_url = "https://ip.jiangxianli.com/?page=%d" % i
        print(base_url)
        crwal_page(base_url)
    writeToFile()