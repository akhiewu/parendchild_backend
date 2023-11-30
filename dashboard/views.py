from django.shortcuts import render
from utils.custom_viewset import CustomViewSet
from utils.response_wrapper import ResponseWrapper
from .serializers import *
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from datetime import datetime
from django.utils import timezone

from django.conf import settings



# Create your views here.

# ............***............ Company ............***............


# class CompanyViewSet(CustomViewSet):
#     serializer_class = CompanyDetailSerializer
#     queryset = Company.objects.all()
#     lookup_field = 'pk'
    
#     def get_serializer_class(self):
#         if self.action in ['subscribe_news_letter']:
#             self.serializer_class = NewsLetterSerializer
            
#         if self.action in ['drop_cv']:
#             self.serializer_class = DropYourCVSerializer

#         if self.action in ['drop_message']:
#             self.serializer_class = MessageSerializer        
#         return self.serializer_class
    
 