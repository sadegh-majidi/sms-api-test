from django.db import models
from django.core.validators import RegexValidator


class Sms(models.Model):
    phone_regex = RegexValidator(regex=r'^\d{11}$',
                                 message="Phone number must be entered in the format: '09011001010'. 11 digits allowed.")
    phone_number_receptor = models.CharField(validators=[phone_regex], max_length=12, verbose_name='receptor')
    message = models.CharField(max_length=150, verbose_name="Message content")
