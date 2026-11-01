from django.urls import path
from .views import URLMappingAPIView

urlpatterns = [
    path("", URLMappingAPIView.as_view(), name="url-mapping"),
    path("<str:short>/", URLMappingAPIView.as_view(), name="url-mapping"),
]
