from rest_framework import views , generics , status , permissions , response

from company.models import Company , Employee


from .serializers import CompanySerializers , EmployeeSerializers

# Api for create new company, A user can create only one company
class CreateCompany(generics.CreateAPIView):
    serializer_class = CompanySerializers
    permission_classes = [permissions.IsAuthenticated,]

    def post(self , request , *args , **kwargs):
        user = request.user
        request.data['owner'] = request.user.id
        company_qs = Company.objects.select_related("owner").filter(owner = user).first()
        if company_qs:
            return response.Response({"data" : {
                "msg" : "A user cannot create more than one company",
                "statusCode" : 400
            }} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CompanySerializers(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = user)
            return response.Response({"data" : {
                "msg" : "A company created successfully!!",
                "statusCode" : 201,
                "meta" : serializer.data
            }} , status=status.HTTP_201_CREATED)
        return response.Response({"data" : {
            "msg" : "error occured when creating company",
            "meta" : serializer.errors,
            "statusCode" : 400
        }} , status=status.HTTP_400_BAD_REQUEST)
   

# Api for create new employee and get all employee list
class AddOrGetEmployees(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializers
    permission_classes = [permissions.IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        company_qs = Company.objects.select_related("owner").filter(owner = request.user).first()
        employee_qs = Employee.objects.select_related("company").filter(company = company_qs)
        serializer = EmployeeSerializers(employee_qs , many = True) 
        return response.Response({"data" : {
            "total" : len(employee_qs),
            "employee" : serializer.data
        }})
    
    def create(self, request, *args, **kwargs):
        company_qs = Company.objects.select_related("owner").filter(owner = request.user).first()
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(company = company_qs)
            return response.Response({"data" : {
                "msg" : "Employee Added!!",
                "statusCode" : 201,
                "meta" : serializer.data
            }} , status=status.HTTP_201_CREATED)
        return response.Response({"data" : {
            "msg" : "Error occured when creating a employee",
            "statusCode" : 400,
            "meta" : serializer.errors
        }})

