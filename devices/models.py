from django.db import models
from django.contrib.auth.models import User

from company.models import Company

class Device(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Printer")
    price = models.IntegerField(default=999)
    purchased_at = models.DateField(blank= True , null=True , editable=True)

    def __str__(self) -> str:
        return self.company.name