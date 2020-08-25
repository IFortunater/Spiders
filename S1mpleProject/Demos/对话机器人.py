import requests

def jarvis(message):
    while message != "拜拜":
        url = "http://tool.mkblog.cn/robot/new.php?word={}".format(message)
        response = requests.get(url)
        reply = response.json()
        print("jarvis:" + reply['text'])
        message = input("Me:")


def qingyunke(message):
    while message != "拜拜":
        url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(message)
        response = requests.get(url)
        reply = response.json()
        print("qingyunke:" + reply['content'])
        message = input("Me:")


def ownthink(message):
    while message != "拜拜":
        url = "https://api.ownthink.com/bot?appid=xiaosi&spoken={}".format(message)
        response = requests.get(url)
        reply = response.json()
        print("ownthink:" + reply['data']['info']['text'])
        message = input("Me:")


if __name__ == '__main__':
    answer = ""
    while answer != "no" or answer != 'No':
        print("请选择聊天机器人:1.jarvis 2.qingyunke 3.ownthink")
        message = input("你的选择:")
        if message == "1":
            message = input("Me:")
            jarvis(message)
        elif message == "2":
            message = input("Me:")
            qingyunke(message)
        elif message == "3":
            message = input("Me:")
            ownthink(message)
        else:
            print("别皮，认真输入")
            continue
        print("还想试试别的机器人嘛？")
        answer = input("yes/no?")






