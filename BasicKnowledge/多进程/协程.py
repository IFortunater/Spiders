import asyncio

async def request(url):
    print("正在请求的url是：", url)
    print("请求成功")
    return url

c = request("www.baidu.com")

# # 创建一个任务循环对象
# loop = asyncio.get_event_loop()
# # 向任务循环对象中添加或者注册一个携程对象，然后然后启动loop
# loop.run_until_complete(c)

# task的创建和使用
# loop = asyncio.get_event_loop()
# 基于loop创建task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# futher的使用
# loop = asyncio.get_event_loop()
# futher = asyncio.ensure_future(c)
# print(futher)
# loop.run_until_complete(futher)
# print(futher)

def callback_func(task):
    # result 返回的就是此任务对象中所封装的携程对象对应的函数的返回值
    print(task.result())
# 绑定回调
loop = asyncio.get_event_loop()
futher = asyncio.ensure_future(c)
# 将回调函数绑定在任务中
futher.add_done_callback(callback_func)
loop.run_until_complete(futher)
