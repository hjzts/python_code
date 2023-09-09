import requests


url = 'https://learnywhere.cn/bb/activity/article/2020/0619/news' \
          '?key=108039b518584c6cacafaafa7712bec4&feat=u47617382&sha' \
          're_platform=wechat&show_user_info=1'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (K'
                      'HTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
    }
response = requests.get(url, headers=headers)
print(response.text)
# url = 'https://www.baidu.com'
# url = 'https://github.com/hjzts'

# session = requests.Session()
# session.post(url)
# request_cookies = session.cookies.get_dict()
# print(request_cookies)

# headers = {
#     # 从浏览器中复制过来的User-Agent
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#     # 从浏览器中复制过来的Cookie
#     'Cookie':''
# }

# resp = requests.get(url,headers=headers)
# print(resp.text)
# response = requests.get(url)
# print(response.request._cookies)
# url = 'https://www.baidu.com/s?wd=python'
# url = 'https://www.baidu.com/s?'
# kw={'wd':'python'}

# response = requests.get(url,headers = headers,params=kw)
# print(response.content)
# print(response.content.decode())
# print(response.request.headers)
# print(response.text)
# print(response.content.decode())          # 注意这里！
# print(response.url)                         # 打印响应的url
# print(response.status_code)                 # 打印响应的状态码
# print(response.request.headers)             # 打印响应对象的请求头
# print(response.headers)                     # 打印响应头
# print(response.request._cookies)            # 打印请求携带的cookies
# print(response.cookies)                     # 打印响应中携带的cookies