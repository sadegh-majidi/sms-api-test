from rest_framework import serializers
from .models import Sms
from .tasks import send_sms


class SmsSerializer(serializers.ModelSerializer):
    def save(self):
        send_sms.delay(self.validated_data['message'], self.validated_data['phone_number_receptor'])
        Sms.objects.create(
            message=self.validated_data['message'],
            phone_number_receptor=self.validated_data['phone_number_receptor']
        )

    class Meta:
        model = Sms
        fields = ['phone_number_receptor', 'message']
