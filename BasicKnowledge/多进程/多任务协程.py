import asyncio
import time

async def request(url):
    print("正在下载", url)
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    # 在asyncio中遇到阻塞，必须手动挂起，用await
    await asyncio.sleep(2)
    print("下载完毕")

urls = [
    'www.baidu.com',
    'www.google.com',
    'www.alibaba.com'
]

start_time = time.time()
# 任务列表， 需要存放多个任务对象
tasks = []
for url in urls:
    c = request(url)
    futher = asyncio.ensure_future(c)
    tasks.append(futher)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait当中
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print("用时:", end_time-start_time)