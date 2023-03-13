from django.urls import path
from .views import CreateCompany , AddOrGetEmployees

urlpatterns = [
    path('create', CreateCompany.as_view(), name='create_company'),
    path('employee', AddOrGetEmployees.as_view(), name='getoradd_employee'),
]