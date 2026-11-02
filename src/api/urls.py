from django.urls import path
from .views import URLMappingCreateAPIView, URLMappingRetrieveAPIView

urlpatterns = [
    path("", URLMappingCreateAPIView.as_view(), name="url-mapping"),
    path("<str:short>/", URLMappingRetrieveAPIView.as_view(), name="url-mapping"),
]
