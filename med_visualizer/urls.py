
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Medical Data Visualizer API",
        default_version='v1',
        description="API documentation for the Medical Data Visualizer project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="olacodeire@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients/', include('health_care.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='swagger-redoc'),
]
