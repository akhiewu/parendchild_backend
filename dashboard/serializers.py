from .models import *
from rest_framework import serializers
from django.utils.html import strip_tags
      

# ............***............ Child Description .....****.......


class ChildDescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = '__all__'
        

# ............***............ Parent .....****...................................

class ParentSerializer(serializers.ModelSerializer):
    parent_description = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Parent
        fields = '__all__'

    def get_parent_description(self,obj):
        serializer = ChildDescriptionSerializer(
            obj.parent_descriptions, many=True)
        return serializer.data        
    
  
# ............***............Start Company ............***......................


class CompanyDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Company
        fields = '__all__'

    def get_logo_url(self,obj):
        if obj.logo:
            file_name = obj.logo
            return ' '+str(file_name)
        else:
            return None

    def get_parent(self,obj):
        serializer = ParentSerializer(
            obj.parents.last())
        return serializer.data
