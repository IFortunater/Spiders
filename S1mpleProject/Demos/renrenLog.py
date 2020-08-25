import re
import requests
from lxml import etree

# url的时间戳
# time = datetime.now()
# year = time.year
# month = time.month - 1
# day = time.day - 5
# hour = time.hour
# second = time.second
# utcSecond = datetime.utcnow().second
# uniqueTimestamp = '{}{}{}{:0>2}{:0>2}{:0>2}'.format(year, month, day, hour, second, utcSecond)
# print(uniqueTimestamp)

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020601642253"
# data数据
data = {
    'email': '18845163672',
    'password': 'xue710869033',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'f': ''
}
# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
# 使用会话
session = requests.session()
response = session.post(url=url, data=data, headers=headers)
cookies = str(response.cookies)
id_pattern = re.compile('id=(\d*?) for')
id = id_pattern.findall(cookies)[0]
print(id)
print(response.status_code)
page_text = response.json()
home_profile_url = page_text['homeUrl'][0:-4] + id + '/profile'
print(home_profile_url)
# 进行第二次请求
response = session.get(url=home_profile_url, headers=headers)
page_text = response.text
with open("../DemoFiles/renren.html", 'w', encoding='utf-8') as fp:
    fp.write(page_text)
fp.close()
html = etree.HTML(response.text)
school = html.xpath('//div[@class="tl-information"]//li[1]/span/text()')[0]
sex = html.xpath('//div[@class="tl-information"]//li[2]/span[1]/text()')[0]
birth = html.xpath('//div[@class="tl-information"]//li[2]/span[2]/text()')[0]
address = html.xpath('//div[@class="tl-information"]//li[3]/text()')[0]
print(school)
print(sex)
print(birth)
print(address)
