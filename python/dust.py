import requests

token = '1574372524:AAGt1bOq9Ljz2KWkHJlfm2GyLvz9_tIQdZQ'
chat_id = '1587872815'
base_url = f'https://api.telegram.org/bot{token}'

#key = '0AOzI%2FXXs1BYC%2BBVUr5B%2F6GHRnJh0QHf6DvVn39hC0%2Fhla9NDnfEP%2BU%2Bof3OdtZYH4GNNvXXPapJDjspPotxLw%3D%3D'
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=0AOzI%2FXXs1BYC%2BBVUr5B%2F6GHRnJh0QHf6DvVn39hC0%2Fhla9NDnfEP%2BU%2Bof3OdtZYH4GNNvXXPapJDjspPotxLw%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%8C%80%EC%A0%84&ver=1.0'

json_data = requests.get(url).json()
pm10Value = json_data['response']['body']['items'][0]['pm10Value']
sinoName = json_data['response']['body']['items'][0]['sidoName']

#sidoNameDML 미세먼지 농도는 pm10value입니다.
#print(f'노은동의 미세먼지 농도는 {pm10Value} 입니다')
dust = f'{sinoName}의 미세먼지 농도는 {pm10Value}입니다.'


#api_url = f'{base_url}/getMe'
api_url = f'{base_url}/sendMessage?chat_id={chat_id}&text={dust}.'

response = requests.get(api_url).json()
print(response)

