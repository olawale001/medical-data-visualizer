from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalRecordViewSet
from .views import medical_data_chart, patient_data_analytics
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'records', MedicalRecordViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)), 
    path('api/chart/', medical_data_chart, name='medical-data-chart'),
    path('api/analytics/', patient_data_analytics, name='patient_data_analytics'),
]
