from django.db import models
from django.contrib.auth.models import User

class MetaData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Company(MetaData):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , default="SPACE X")
    company_vision = models.TextField(blank=True , null=True)
    establised_data = models.DateField(editable=True , blank=True , null=True)

EMPLOYEE_DESIGNATION = (
    ("manager" , "Manager"),
    ("owner" , "Owner"),
    ("etc" , "ETC")
)

class Employee(MetaData):
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , default="SPACE X")
    designation = models.CharField(max_length=20 , choices=EMPLOYEE_DESIGNATION , blank=True , null= True)

