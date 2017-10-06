# -*- coding: utf-8 -*-
import os

from doco.client import Client


class DocomoDialogAPI(object):

    def __init__(self, api_key=None):
        #api_key = os.environ.get('482f48562f66455734633370765a6e4a66624e64343553667a44383857775047732e725250643651344d35', api_key)
        api_key = '482f48562f66455734633370765a6e4a66624e64343553667a44383857775047732e725250643651344d35'
        self.__client = Client(apikey=api_key)

    def reply(self, text):
        response = self.__client.send(utt=text, apiname='Dialogue',t=20)
        utt = response['utt']

        return utt
