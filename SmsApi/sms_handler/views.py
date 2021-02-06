from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import SmsSerializer
from .models import Sms
from django.shortcuts import reverse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class NewSmsFormApiView(APIView):
    template_name = 'sms_handler/index.html'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({})


class SmsSenderApiView(CreateAPIView):
    serializer_class = SmsSerializer
    queryset = Sms.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to=reverse('sms_handler:new_form'))
