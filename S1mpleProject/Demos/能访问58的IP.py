import requests
from multiprocessing.pool import Pool

IP_Pool = []
url = "https://bj.58.com/chaoyang/chuzu/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
}


def read_IP():
    with open("../../BasicKnowledge/IP_Pool.txt", 'r', encoding='utf-8') as f:
        IP_pool = f.readlines()
        f.close()
    IP_pool = [x.strip() for x in IP_pool]
    return IP_pool


def Test(proxy):
    try:
        print(proxy, "正在测试")
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy
        }
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        if "二手房" in response.text:
            print(proxy, "是有效的")
            with open("58有效IP.txt", 'a', encoding='utf-8') as f:
                f.write(proxy)
        else:
            print(proxy, "是无效的")
    except:
        pass


if __name__ == '__main__':
    IP_Pool = read_IP()
    pool = Pool(4)
    print("开始测试")
    print(IP_Pool)
    pool.map(Test, IP_Pool)
    pool.close()
    pool.join()