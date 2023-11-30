from django import forms
from .models import *
from django.conf import settings
import re
from django.core.exceptions import ValidationError
from util.helpers import validate_chars, simple_form_widget
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import ImageFieldFile
from django.template.defaultfilters import filesizeformat
import os


# ............***............ Company Description ............***............

class CompanyManageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyManageForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter Company Name...',
            'maxlength': 50
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Enter Company description...',
            
        })
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Enter Company Address...',
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Enter Company Phone Number...',
            'maxlength': 50
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter Company Email...',
            
        })
        self.fields['socials'].widget.attrs.update({
            'placeholder': 'Enter Company Socials...',
            'maxlength': 255
        })
        self.fields['facebook_url'].widget.attrs.update({
            'placeholder': 'Enter Company facebook url...',
            'maxlength': 255
        })
        self.fields['twitter_url'].widget.attrs.update({
            'placeholder': 'Enter Company Twitter Url...',
            'maxlength': 255
        })
        self.fields['instagram_url'].widget.attrs.update({
            'placeholder': 'Enter Company Instagram Url...',
            'maxlength': 255
        })
        self.fields['linkedin_url'].widget.attrs.update({
            'placeholder': 'Enter Company Linkedin Url...',
            'maxlength': 255
        })

    class Meta:
        model = Company
        fields = '__all__'
        
  

# ............***............ Parent ............***............


class ParentManageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParentManageForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Enter Parent first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Enter Parent last name...',
        })
        
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Enter Parent address',
        })
        self.fields['street'].widget.attrs.update({
            'placeholder': 'Enter Parent street road',
        })
        self.fields['city'].widget.attrs.update({
            'placeholder': 'Enter Parent city',
        })
        self.fields['state'].widget.attrs.update({
            'placeholder': 'Enter Parent state',
        })
        self.fields['zip'].widget.attrs.update({
            'placeholder': 'Enter Parent zip code',
        })
              

    class Meta:
        model = Parent
        fields = '__all__'  
        
# ............***............ Child Description ............***............                    
  
class ChildDescriptionManageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChildDescriptionManageForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Enter ChildDescription first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Enter ChildDescription last name',
        })
              

    class Meta:
        model = Child
        fields = '__all__'        
        
