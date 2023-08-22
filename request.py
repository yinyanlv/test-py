import requests

response = requests.get('https://www.baidu.com')

print('Content-Type: {}'.format(response.headers['Content-Type']))