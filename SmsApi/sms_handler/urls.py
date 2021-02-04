from django.urls import path
from .views import send_sms


app_name = 'sms_handler'

urlpatterns = [
    path('send/', send_sms, name='send'),
]
