from django.urls import path
from .views import SmsSenderApiView, NewSmsFormApiView


app_name = 'sms_handler'

urlpatterns = [
    path('send/', SmsSenderApiView.as_view(), name='send'),
    path('new/', NewSmsFormApiView.as_view(), name='new_form')
]
