from django.db import models
from django.utils import timezone
from company.models import Company, Employee
from devices.models import Device

CONDITION_WHEN_CHECKOUT = (
    ("good", "Good"),
    ("bad", "Bad")
)

# TODO : Add more option
CONDITION_WHEN_RETURN = (
    ("good", "Good"),
    ("bad", "Bad")
)


class DeviceShare(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    share_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    condition_when_checkout = models.CharField(
        max_length=10, choices=CONDITION_WHEN_CHECKOUT, default="good")
    condition_when_return = models.CharField(
        max_length=10, null=True, choices=CONDITION_WHEN_RETURN)

    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.device.name} Shared with {self.employee.name}"