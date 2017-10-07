# -*- coding: utf-8 -*-
import os

from doco.client import Client


class DocomoDialogAPI(object):

    def __init__(self, api_key=None):
        api_key = 'API KEY'
        self.__client = Client(apikey=api_key)

    def reply(self, text):
        response = self.__client.send(utt=text, apiname='Dialogue',t=20)
        utt = response['utt']

        return utt
