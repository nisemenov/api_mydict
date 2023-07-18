import requests
from pprint import pprint

url = 'http://127.0.0.1:8000/api/v1/api-token-auth/'
data = {
    'username': 'admin_1',
    'password': 'boy95166',
}

token = requests.post(url, data=data).json()['token']

url = 'http://127.0.0.1:8000/api/v1/posts/5/comments/8/'
head = {
    'Authorization': f'Token {token}'
}
data = {
    'text': 'test',
}
# requests.delete(url, data=data, headers=head)

url = 'http://127.0.0.1:8000/api/v1/posts/'
r = requests.get(url)
pprint(r.json())
