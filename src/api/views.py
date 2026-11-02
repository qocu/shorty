from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from mappings.models import URLMapping
from .serializers import URLMappingSerializer


__all__ = ["URLMappingCreateAPIView", "URLMappingRetrieveAPIView"]

class URLMappingMixin:
    serializer_class = URLMappingSerializer
    queryset = URLMapping.objects.all()

class URLMappingCreateAPIView(URLMappingMixin, APIView):
    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class URLMappingRetrieveAPIView(URLMappingMixin, APIView):
    def get(self, request, short: str) -> Response:
        mapping = get_object_or_404(self.queryset, short=short)
        serializer = self.serializer_class(mapping)
        return Response(serializer.data)
