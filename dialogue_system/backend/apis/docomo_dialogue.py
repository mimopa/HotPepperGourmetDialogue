# -*- coding: utf-8 -*-
import os

import requests
import json
import types
from doco.client import Client

api_key = os.environ.get('DOCOMO_DIALOGUE_API_KEY')
appid = os.environ.get('DOCOMO_DIALOGUE_API_KEY')
class DocomoDialogAPI(object):
    
    def __init__(self, api_key=None):
        api_key = os.environ.get('DOCOMO_DIALOGUE_API_KEY')
        # self.__client = Client(apikey=api_key)

    def reply(self, text):
        #response = self.__client.send(utt=text, apiname='Dialogue',t=20)
        
        endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'
        url = endpoint.replace('REGISTER_KEY', api_key)
        #text = message.body['text'] 
        
        payload = {'language':'ja-JP', 'botId':'Chatting','appId':appid,'voiceText':text, 'clientData': {'option': {'t': 'kansai'}}}
        headers = {'Content-type': 'application/json'}

        #送信
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        data = r.json()

        #jsonの解析
        #utt = data['utt']
        utt = data['systemText']['utterance']
        #utt = response['utt']

        return utt
