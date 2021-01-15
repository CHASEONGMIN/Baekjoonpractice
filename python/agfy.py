##https://api.agify.io/?name=seongmin  API활용 실습

import requests

url = 'https://api.agify.io/?name=seongmin'

#.json() -> json 문서를 바로 python dict 형태로 변환
response = requests.get(url).json()

print(response)
print(type(response)) # type은 문자열이다.

name = response['name']
age = response['age']

print(f'{name}의 나이는 {age}입니다.')
