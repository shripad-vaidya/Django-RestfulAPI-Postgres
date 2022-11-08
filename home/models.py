from pyexpat import model
from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    salary=models.CharField(max_length=100)
   
    class Meta:
        db_table="tbl_emp_data"