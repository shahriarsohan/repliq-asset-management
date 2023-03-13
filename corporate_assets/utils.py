from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Api Documentation Repliq Assets management Api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@sohan.onion"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)