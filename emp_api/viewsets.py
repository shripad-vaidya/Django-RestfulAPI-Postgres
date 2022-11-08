from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViews(viewsets.ModelViewSet):
    queryset=models.EmpModel.objects.all()
    serializer_class=serializers.EmmployeeSerializer
    
#list(),Retrive(),create(),update(),destory()
