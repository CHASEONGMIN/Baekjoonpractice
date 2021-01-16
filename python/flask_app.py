
# A very simple Flask Hello World app for you to get started with...
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'WEb study using Flask!'

#챗봇이 메시지를 받으면 여기에서 업데이트 내용을 확인할거임.
@app.route('/ssafy')
def ssafy():
    # 누가 메시지를 보냈는지 확인 -> chat_id를 확인

    # 어떤 메시지를 보냈는지 확인 (미세먼지)

    #메시지에 따라서 다른 답변을 chat_id에 전송
        

    return True