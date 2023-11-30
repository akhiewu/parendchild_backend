from django.urls import path
from .views import *
from .admin_views import *
from dashboard import views

admin_panel_urlpatterns = [
    path('', index, name= 'index'),
    path('company-profile', company_profile, name= 'company_profile'),
    path('company_profile_update/<id>/', company_profile_update, name= 'company_profile_update'),
    

     #.............***................ Parent ...................***................
    
    path('parent-list/', parent_list, name= 'parent_list'),
    path('parent-create/', parent_create, name= 'parent_create'),
    path('parent-update/<id>/', parent_update, name= 'parent_update'),
    path('parent-details/<id>/', parent_details, name= 'parent_details'),
    
     #.............***................ Child ...................***................
    
    path('child-description-list/', child_description_list, name= 'child_description_list'),
    path('child-description-create/', child_description_create, name= 'child_description_create'),
    path('child-description-update/<id>/', child_description_update, name= 'child_description_update'),
    path('child-description-details/<id>/', child_description_details, name= 'child_description_details'),
    
    
]    
 

urlpatterns =[
   # path('home_details/', CompanyViewSet.as_view({'get': 'home_details'}), name="home_details"),
    
]+ admin_panel_urlpatterns 
