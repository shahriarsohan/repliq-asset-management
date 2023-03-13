from rest_framework import serializers

from company.api.serializers import CompanySerializers , EmployeeSerializers
from devices.api.serializers import DeviceSerializer

from distribute.models import DeviceShare

class CreateDeviceShareSerializers(serializers.ModelSerializer):

    class Meta:
        model = DeviceShare
        fields = ('__all__')

    
class DeviceShareSerializers(serializers.ModelSerializer):
    company = CompanySerializers(many = False)
    employee = EmployeeSerializers(many = False)
    device = DeviceSerializer(many = False)

    class Meta:
        model = DeviceShare
        fields = ('__all__')