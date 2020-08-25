# 百度翻译：
#     - post请求（携带了参数）
#     - 相应数据是一组json数据
import requests
import json

url = "https://fanyi.baidu.com/sug"
kw = input("Please Input keyword:")
data = {
    'kw': kw,
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
response = requests.post(url=url, data=data, headers=headers)
# 直接返回json对象，且得确定相应的数据必须是json串，否则报错。
# 查看是否是返回json数据可以查看Response Headers里面的content-type就是数据类型，若是json即可
result = response.json()
print(result)
fp = open("../DemoFiles/BaiDuTranslateResult.json", 'a+', encoding='utf-8')
json.dump(result, fp=fp, ensure_ascii=False)
fp.write('\n')
print('over')

