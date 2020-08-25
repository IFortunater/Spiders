# __VIEWSTATE: p5O6KXWJ/Gfy4xaRQJIpgTJB2c5Hg7jrQ2pEozOkRPAYMoOBC9h3ltovCHfGxXaWyMSHegRbnAVU2TXLkRhovf5WM6iUtM9dX/34gL/DT440Tnf1wX3Ohi07OXs=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: me_handsomeboy@qq.com
# pwd: xue710869033
# code: 4YOD
# denglu: 登录


import requests
from lxml import etree
from PIL import Image

url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user//RandCode.ashx"
log_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
session = requests.session()
response = session.get(url, headers=headers)
html = etree.HTML(response.text)
VIEWSTATE = html.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
VIEWSTATEGENERATOR = html.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value')[0]
print(VIEWSTATE)
print(VIEWSTATEGENERATOR)
img_url = "https://so.gushiwen.cn/" + html.xpath('//img[@id="imgCode"]/@src')[0]
img_content = session.get(img_url, headers=headers).content
with open("古诗词网验证码.jpg", 'wb') as f:
    f.write(img_content)
    f.close()
img = Image.open("古诗词网验证码.jpg")
print(img.show())
img_text = input("请输入图片内容：")
data = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'me_handsomeboy@qq.com',
    'pwd': 'xue710869033',
    'code': img_text,
    'denglu': '登录'
}
result = session.post(log_url, data=data, headers=headers)
result.encoding = 'utf-8'
print(result.text)
if "我的收藏" in result.text:
    print("登录成功")
else:
    print("登录失败")