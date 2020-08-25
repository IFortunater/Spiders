#%%   ---------单进程----------
import time
import requests

urls = [
    "https://www.pythonanywhere.com/forums/topic/12714/",
    "https://blog.csdn.net/guoziqing506/article/details/52014506",
    "http://httpbin.org/get",
]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


def get_page(url):
    print('正在访问' + url)
    # response = requests.get(url, headers=headers)
    # print("返回的数据程度：", len(response.content))
    time.sleep(2)
    print(url + "请求结束")


if __name__ == '__main__':
    start_time = time.time()
    for url in urls:
        get_page(url)
    end_time = time.time()
    print("总共耗时", end_time-start_time)

#%%      -----------多进程----------
import time
import requests
# 引入进程池类
from multiprocessing.dummy import Pool

urls = [
    "https://www.pythonanywhere.com/forums/topic/12714/",
    "https://blog.csdn.net/guoziqing506/article/details/52014506",
    "http://httpbin.org/get",
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


def get_page(url):
    print('正在访问' + url)
    # response = requests.get(url, headers=headers)
    # print("返回的数据程度：", len(response.content))
    time.sleep(2)
    print(url + "请求结束")


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(3)
    pool.map(get_page, urls)
    end_time = time.time()
    print("总共耗时", end_time - start_time)