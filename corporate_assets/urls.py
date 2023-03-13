from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

from .utils import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.api.urls')),
    path('company/', include('company.api.urls')),
    path('device/', include('devices.api.urls')),
    path('distribute/', include('distribute.api.urls')),

    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
]
