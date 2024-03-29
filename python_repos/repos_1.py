"""
执行API调用并处理结果，找出GitHub上星级最高的Python项目
"""

import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)#状态码200表示请求成功

#将API响应存储在一个变量中
response_dict = r.json()

#处理结果
print(response_dict.keys())
