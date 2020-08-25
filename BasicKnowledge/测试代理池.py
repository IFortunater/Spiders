import requests
from multiprocessing.pool import Pool


class TestIPPool:
    ip_pool = []

    def make_ip_pool(self):
        with open("./IP_Pool.txt", 'r', encoding='utf-8') as fp:
            self.ip_pool = fp.readlines()
            fp.close()

    def crawl(self):
        for proxy in self.ip_pool:
            proxy = proxy[:-1]
            print(proxy + "开始测试")
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
            }
            url = 'https://www.baidu.com/'
            try:
                response = requests.get(url, headers=headers, timeout=5, proxies=proxies)
                print(response.text)
                print(proxy + "是有效的")
            except:
                print(proxy + "是无效的")
                pass

    def crawl2(self, proxy):
        proxy = proxy[:-1]
        print(proxy + "开始测试")
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        url = 'https://www.baidu.com/'
        try:
            response = requests.get(url, headers=headers, timeout=5, proxies=proxies)
            print(response.text)
            print(proxy + "是有效的")
        except:
            print(proxy + "是无效的")
            pass

    def Test(self):
        pool = Pool(4)
        self.make_ip_pool()
        pool.map(self.crawl2, self.ip_pool)
        pool.join()
        # self.crawl()


if __name__ == '__main__':
    t = TestIPPool()
    t.Test()
