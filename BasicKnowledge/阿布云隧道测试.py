import requests

url = 'http://httpbin.org/get'

# 代理服务器
proxy_host = 'proxy.abuyun.com'
proxy_port = '9020'

# 代理隧道验证信息
proxy_user = 'H8U61RTM72Q1J85D'
proxy_pass = 'B83C3EF0F8E8B0A2'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass,
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta,
}
for i in range(5):
    response = requests.get(url, proxies=proxies)
    print(response.status_code)
    print(response.text)