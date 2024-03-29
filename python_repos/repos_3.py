"""
提取repo_dict中与一些键相关联的值
"""

import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)#状态码200表示请求成功

#将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#搜索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print('Name:',repo_dict['name'])#首先要知道其中的键
print('Owner:',repo_dict['owner']['login'])
print('Stars:',repo_dict['stargazers_count'])
print('Repository:',repo_dict['html_url'])
print('Created:',repo_dict['created_at'])
print('Updated:',repo_dict['updated_at'])
print('Description:',repo_dict['description'])
