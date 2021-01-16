import requests

text = input()

token = '1574372524:AAGt1bOq9Ljz2KWkHJlfm2GyLvz9_tIQdZQ'
chat_id = '1587872815'
base_url = f'https://api.telegram.org/bot{token}'

#api_url = f'{base_url}/getMe'
api_url = f'{base_url}/sendMessage?chat_id={chat_id}&text={text}.'

response = requests.get(api_url).json()
print(response)