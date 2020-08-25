import re
import requests
from lxml import etree
from multiprocessing.dummy import Pool

base_url = "https://www.pearvideo.com/category_5"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
urls = []
#  原则：线程池只针对阻塞且耗时的操作
def parse_first_page(url):
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    hrefs = html.xpath('//ul[@id="listvideoListUl"]/li[@class="categoryem "]/div/a/@href')
    titles = html.xpath('//ul[@id="listvideoListUl"]/li[@class="categoryem "]/div/a/div[2]/text()')
    for href, title in zip(hrefs, titles):
        href = 'https://www.pearvideo.com/' + href
        mv_title = title + ".mp4"
        mv_page = requests.get(href, headers=headers)
        pattern = re.compile('srcUrl="(.*?)"')
        mv_url = pattern.findall(mv_page.text)[0]
        # print(mv_title, mv_url)
        mv_info_dict = {
            'title': mv_title,
            'url': mv_url,
        }
        urls.append(mv_info_dict)


def download(mv_info_dict):
    title = mv_info_dict['title']
    mv_url = mv_info_dict['url']
    print(title + "开始下载")
    response = requests.get(mv_url, headers=headers).content
    with open(title, 'wb') as f:
        f.write(response)
        f.close()
    print(title + "下载完成")


if __name__ == '__main__':
    parse_first_page(base_url)
    print("----------------------------------------")
    pool = Pool(3)
    pool.map(download, urls)
    pool.close()
    pool.join()