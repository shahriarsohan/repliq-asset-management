from django.urls import path
from .views import (
    TotalSharedDeviceView,
    ActiveSharedDevices,
    ShareDeviceView,
    ReturnDeviceView,
)

urlpatterns = [
    path("total-shared", TotalSharedDeviceView.as_view(),
         name="total-device-shared-till-date"),
    path("active-shared", ActiveSharedDevices.as_view(),
         name="active-device-shared"),
    path("share-device", ShareDeviceView.as_view(), name="new-device-share"),
    path("return-device/<id>", ReturnDeviceView.as_view(), name="return-device-share"),
]
