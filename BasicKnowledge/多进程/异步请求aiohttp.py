import requests
import asyncio
# 使用该模块中的ClientSession模块
import aiohttp
import time

urls = [
    'https://www.baidu.com',
    'https://www.jd.com',
    'http://mepromise.top',
    'https://www.taobao.com',
    'http://httpbin.org/get'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

start = time.time()
async def get_page(url):
    print("正在下载", url)
    # resquest基于同步网络的请求，会中断协程的异步。必须使用aiohttp进行异步网络的请求
    # aiohttp：基于异步网络请求的模块
    # response = requests.get(url, headers=headers)
    # page = response.text
    async with aiohttp.ClientSession() as session:
        async with await session.get(url, headers=headers) as response:
            # text()返回的是字符串形式的数据
            # read()返回的是二进制数据
            # json()返回的是json格式的数据
            # 注意：在获取数据响应数据之前一定要用await进行手动挂起
            page = await response.text()
    print("下载完毕", url)

tasks = []
for url in urls:
    c = get_page(url)
    futher = asyncio.ensure_future(c)
    tasks.append(futher)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print("耗时：", end-start)