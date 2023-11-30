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


class CompanyViewSet(CustomViewSet):
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        if self.action in ['subscribe_news_letter']:
            self.serializer_class = NewsLetterSerializer
            
        if self.action in ['drop_cv']:
            self.serializer_class = DropYourCVSerializer

        if self.action in ['drop_message']:
            self.serializer_class = MessageSerializer        
        return self.serializer_class
    
    # ............*** .......... Home page .........***...........
    
    def home_details(self, request, *args, **kwargs):
        home_page_qs = Company.objects.all().last()
        if not home_page_qs:
            return ResponseWrapper(error_msg='Home Page Details Not Found', status=400)
        serializer = CompanyDetailSerializer(instance=home_page_qs)
        return ResponseWrapper(data=serializer.data, msg='Success')
    
    
# ..............***..........Email..................***................................

    def subscribe_news_letter(self, request, *args, **kwargs):
    
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors, error_code=400)
        email = request.data.get('email')
        news_letter_qs = NewsLetter.objects.filter(email = email).last()
        if news_letter_qs:
            serializer = NewsLetterSerializer(instance=news_letter_qs)
            return ResponseWrapper(status=400, msg='Already Subscribed')
        qs = serializer.save()
        email_to = qs.email
        mail_from = settings.EMAIL_HOST_USER
        mail_text = 'Please do not Reply'
        mail_subject= "Welcome to Frame!"
        today = timezone.now().date()
        name = email_to.split('@')[0]
        html_content = "Dear " + name + ", <br><br>Thanks for joining Frame. We are glad to add another member to our growing family. \
                You will receive all the latest news headlines, industry trends, and blog posts by Frame here.<br><br>Stay Tuned!<br> --<br> \
                Frame SDN BHD (1202790-W) <br>\
                B2-3-13A, Solaris Dutamas, No. 1, Jalan Dutamas 1, 50480, Dhaka, Bangladesh <br>\
                Visit us: https://www.frame.com/ <br>\
                Frame operates in the field of IT with the aim to push the world towards digitization,\
                by conducting business with government agencies. Frame streamlines<br> \
                seamless guidance and implementation of E-Commerce, E-Payment, E-Financial Services, and many more digital solutions to create e-government with a trusted identity."

        msg = EmailMultiAlternatives(
            mail_subject, mail_text, mail_from, [email_to]
        )
        
        msg.attach_alternative(html_content, "text/html") 
        msg.send()
        serializer = NewsLetterSerializer(instance=qs)
        return ResponseWrapper(data=serializer.data, msg='created')  

    def job_circular_list(self,request, *args, **kwargs):
        latest_job_circular_qs = Career.objects.all().last()
        if not latest_job_circular_qs:
            return ResponseWrapper(error_msg=['No Job Are Available Now'], status=400)
        serializer = JobCircularDetailsSerializer(instance=latest_job_circular_qs )
        return ResponseWrapper(data=serializer.data, msg='Success')

    def drop_cv(self, request, *args, **kwargs):
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        file = request.data.get('file')
        body = request.data.get('body')
        job_circular = request.data.get('job_circular')
        email_qs = DropCV.objects.filter(email = email)

        if email_qs:
            return ResponseWrapper(error_msg=['Email Address Already Provided'], error_code=400)

        drop_cv = DropCV.objects.create(name = name,job_circular_id = job_circular,phone = phone, email = email, body = body,file=file )

        serializer = DropYourCVSerializer(instance=drop_cv)
        return ResponseWrapper(data=serializer.data, msg='Success', status=200)

    def drop_message(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')
        if not name:
            return ResponseWrapper(error_msg=['Name is Not Given'], error_code=400)
        message_qs = Message.objects.create(name=name, email=email,
                                             message=message)

        serializer = MessageSerializer(instance=message_qs)
        return ResponseWrapper(data=serializer.data, msg='Success', status=200)           
       