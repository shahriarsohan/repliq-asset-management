from rest_framework import serializers

from company.api.serializers import CompanySerializers , EmployeeSerializers
from devices.api.serializers import DeviceSerializer

from distribute.models import DeviceShare

class CreateDeviceShareSerializers(serializers.ModelSerializer):

    class Meta:
        model = DeviceShare
        fields = ('__all__')

# This searializer will provide better readability (Both serializer can be merge into one but will introduce unnecessary complexity)
class DeviceShareSerializers(serializers.ModelSerializer):
    company = CompanySerializers(many = False)
    employee = EmployeeSerializers(many = False)
    device = DeviceSerializer(many = False)

    class Meta:
        model = DeviceShare
        fields = ('__all__')