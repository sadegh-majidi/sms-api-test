from celery import shared_task
from kavenegar import *


@shared_task
def send_sms(message, receptor):
    api = KavenegarAPI('775A3371715A71336C7763436A6555746C6D614E4758636A6548386949516578424B3675686F454F7A33513D')
    params = {'sender': '1000596446', 'receptor': receptor, 'message': message}
    response = api.sms_send(params)
    return response
