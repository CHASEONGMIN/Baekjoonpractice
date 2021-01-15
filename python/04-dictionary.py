#Dictionary 선언
my_home = {
    #key: value
    'location': 'daejeon',
    'class': '2',
    'name': '차성민', 
    # 마지막에는 혹시 모르니 ,를 써주는게 좋음(trailing comma)
}

#원소 접근 -> dict['key']
print(my_home['location'])
print(my_home['class'])
print(my_home['name'])

#원소 접근 2 ->  dict.get('key')
print(my_home.get('location'))
print(my_home.get('class'))
print(my_home.get('name'))


#원소 변경
my_home['location'] = 'Daejeon'
print(my_home['location'])

#미니 실습
# 1-1 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만드시오.
# (name, age, msg)

my_info = {
    'name': '차성민',
    'age': '27',
    'greeting': '잘부탁드려요',
    'msg':{
        'one':'안녕',
        'two': '하세요',
    },
    'hobbies': [
        'soccer',
        'movie',
        ],
}

# 1-2 my_info에서 나이 값을 출력하시오
print(my_info['age'])
print(my_info.get('age'))


############################################
print(my_info['msg'])  #{'one': '안녕', 'two': '하세요'}
print(my_info['msg']['one']) #안녕

print(my_info['hobbies']) #soccer, movie
print(my_info['hobbies'][0]) #soccer

