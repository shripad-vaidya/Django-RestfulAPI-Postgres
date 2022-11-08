#api -> data in .json format
from dataclasses import field, fields
from rest_framework import serializers
from .models import EmpModel

class EmmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpModel
        fields='__all__'
        
