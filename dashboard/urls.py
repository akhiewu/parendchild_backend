from django.urls import path
from .views import *
from .admin_views import *
from dashboard import views

admin_panel_urlpatterns = [
    path('', index, name= 'index'),
    path('company-profile', company_profile, name= 'company_profile'),
    path('company_profile_update/<id>/', company_profile_update, name= 'company_profile_update'),
    

     #.............***................ Vision ...................***................
    
    path('vision-list/', vision_list, name= 'vision_list'),
    path('vision-create/', vision_create, name= 'vision_create'),
    path('vision-update/<id>/', vision_update, name= 'vision_update'),
    path('vision-details/<id>/', vision_details, name= 'vision_details'),
    
     #.............***................ Vision Description ...................***................
    
    path('vision-description-list/', vision_description_list, name= 'vision_description_list'),
    path('vision-description-create/', vision_description_create, name= 'vision_description_create'),
    path('vision-description-update/<id>/', vision_description_update, name= 'vision_description_update'),
    path('vision-description-details/<id>/', vision_description_details, name= 'vision_description_details'),
    
    
]    
 

urlpatterns =[
    path('home_details/', CompanyViewSet.as_view({'get': 'home_details'}), name="home_details"),
    path('subscribe_news_letter/', CompanyViewSet.as_view({'post': 'subscribe_news_letter'}), name='subscribe_news_letter'),
    path('job_circular_list/', CompanyViewSet.as_view({'get': 'job_circular_list'}), name='job_circular_list'),
    path('drop_cv/',CompanyViewSet.as_view({'post': 'drop_cv'}), name='drop_cv'),
    path('drop_message/',CompanyViewSet.as_view({'post': 'drop_message'}), name='drop_message')
]+ admin_panel_urlpatterns 
