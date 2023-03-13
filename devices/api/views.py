from rest_framework import views , generics , status , permissions , response

from company.models import Company 
from devices.models import Device
from .serializers import DeviceSerializer

class AddOrGetDevices(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Device.objects.select_related("user" , "company").filter(user = self.request.user)
        return qs
    
    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = DeviceSerializer(qs , many = True)
        return response.Response({"data" : {
            "total" : len(qs),
            "devices" : serializer.data
        }})
    
    def create(self, request, *args, **kwargs):
        user = request.user
        company_qs = Company.objects.select_related("owner").filter(owner = user).first()
        request.data["user"] = user.id
        request.data["company"] = company_qs.id
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"data" : {
                "msg" : "A device created successfully!!",
                "statusCode" : 201,
                "meta" : serializer.data
            }} , status=status.HTTP_201_CREATED)
        return response.Response({"data" : {
            "msg" : "error occured when creating new device",
            "meta" : serializer.errors,
            "statusCode" : 400
        }} , status=status.HTTP_400_BAD_REQUEST)