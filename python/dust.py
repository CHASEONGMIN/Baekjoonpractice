import requests

key = '0AOzI%2FXXs1BYC%2BBVUr5B%2F6GHRnJh0QHf6DvVn39hC0%2Fhla9NDnfEP%2BU%2Bof3OdtZYH4GNNvXXPapJDjspPotxLw%3D%3D'

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey={key}&returnType=json'

http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey=0AOzI%2FXXs1BYC%2BBVUr5B%2F6GHRnJh0QHf6DvVn39hC0%2Fhla9NDnfEP%2BU%2Bof3OdtZYH4GNNvXXPapJDjspPotxLw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&searchDate=2020-11-14&InformCode=PM10


response = requests.get(url).json()
print(response)