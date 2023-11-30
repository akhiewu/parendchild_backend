from django.db import models
import uuid
from django.utils.text import slugify
from util.utils import (
    time_str_mix_slug
)
from django.db.models.signals import pre_save
from django.conf import settings
from util.helpers import get_dynamic_fields
#from ckeditor_uploader.fields import RichTextUploadingField



# ............***............ Company ............***............

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    logo = models.FileField(upload_to='company', null=True, blank=True)
    socials = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255,null=True, blank=True)
    twitter_url = models.CharField(max_length=255,null=True, blank=True)
    instagram_url = models.CharField(max_length=255,null=True, blank=True)
    linkedin_url = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name


# ............***............ Vision ............***............


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    street = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='parents')

    def __str__(self):
        return self.first_name

# ............***............ Vision Description ............***............


class Child(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    child = models.ForeignKey(Parent, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='childs')

    def __str__(self):
        return self.first_name








    





