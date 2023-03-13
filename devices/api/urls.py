from django.urls import path
from .views import AddOrGetDevices

urlpatterns = [
    path('', AddOrGetDevices.as_view(), name='getoradd_device'),
]