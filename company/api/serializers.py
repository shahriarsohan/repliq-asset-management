from rest_framework import serializers

from company.models import Company , Employee

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class EmployeeSerializers(serializers.ModelSerializer):
    company = CompanySerializers(many = False ,read_only=True)
    class Meta:
        model = Employee
        fields = ('__all__')

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['company'] = CompanySerializers(instance.company).data
       return ret