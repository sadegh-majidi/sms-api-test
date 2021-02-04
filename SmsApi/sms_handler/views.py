from django.shortcuts import render
from kavenegar import *
from django.http import HttpResponse


def send_sms(request):
    api = KavenegarAPI('775A3371715A71336C7763436A6555746C6D614E4758636A6548386949516578424B3675686F454F7A33513D')
    params = {'sender': '1000596446', 'receptor': '09361457810', 'message': 'دستتو بذار تو جیبتو برو.'}
    response = api.sms_send(params)
    return HttpResponse('all good')
