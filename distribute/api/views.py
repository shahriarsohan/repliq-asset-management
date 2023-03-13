from django.utils import timezone
from rest_framework import views, generics, status, permissions, response

from company.models import Company, Employee
from devices.models import Device
from distribute.models import DeviceShare

from .serializers import DeviceShareSerializers , CreateDeviceShareSerializers


class TotalSharedDeviceView(generics.ListAPIView):
    serializer_class = DeviceShareSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        user = self.request.user
        comapny_qs = Company.objects.select_related(
            "owner").filter(owner=user).first()
        return DeviceShare.objects.select_related("company", "employee", "device").filter(company=comapny_qs)

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = DeviceShareSerializers(qs, many=True)
        return response.Response({"data": {
            "total_shared": len(qs),
            "shared_device": serializer.data,
            "statusCode": 200
        }})


class ActiveSharedDevices(generics.ListAPIView):
    serializer_class = DeviceShareSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        user = self.request.user
        comapny_qs = Company.objects.select_related(
            "owner").filter(owner=user).first()
        return DeviceShare.objects.select_related("company", "employee", "device").filter(company=comapny_qs, return_date__lt=timezone.now())

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = CreateDeviceShareSerializers(qs, many=True)
        return response.Response({"data": {
            "total_shared": len(qs),
            "shared_device": serializer.data,
            "statusCode": 200
        }})


class ShareDeviceView(generics.CreateAPIView):
    serializer_class = CreateDeviceShareSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user
        comapny_qs = Company.objects.select_related(
            "owner").filter(owner=request.user).first()
        request.data["company"] = comapny_qs.id
        serializer = CreateDeviceShareSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"data": {
                "msg": "Device shared with a employee",
                "statusCode": 200,
                "meta": serializer.data
            }})
        return response.Response({"data": {
            "msg": "Error occured",
            "statusCode": 400,
            "errors": serializer.errors
        }})


class ReturnDeviceView(generics.UpdateAPIView):
    serializer_class = DeviceShareSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def update(self, request, *args, **kwargs):
        shared_device_obj = DeviceShare.objects.select_related(
            "company", "employee", "device").filter(id=self.kwargs["id"]).get()
        if shared_device_obj:
            # try:
            shared_device_obj.return_date = timezone.now()
            shared_device_obj.condition_when_return = request.data.get("condition_when_return")
            shared_device_obj.notes = request.data.get("notes")
            shared_device_obj.save()
            return response.Response({"data": {
                "msg": "Device Returned Successfully",
                "statusCode": 200,
                }})
            # except Exception as e:
            #     print(e)
            #     return response.Response({"data" : {
            #         "msg" : "Something went wrong",
            #         "statusCode" : 500
            #     }})
        return response.Response({"data" : {
            "msg" : "Device Shared Data Not Found",
            "statusCode" : 404
        }} , status=status.HTTP_404_NOT_FOUND)