
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from mappings.models import URLMapping
from .serializers import URLMappingSerializer


__all__ = ["URLMappingAPIView"]

class URLMappingAPIView(APIView):
    serializer_class = URLMappingSerializer
    queryset = URLMapping.objects.all()

    def get(self, request, short):
        mapping = get_object_or_404(self.queryset, short=short)
        serializer = self.serializer_class(mapping)
        return Response(serializer.data)
