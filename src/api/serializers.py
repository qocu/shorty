from rest_framework import serializers
from mappings.models import URLMapping

__all__ = ["URLMappingSerializer"]


class URLMappingSerializer(serializers.ModelSerializer):
    short = serializers.ReadOnlyField()

    class Meta:
        model = URLMapping
        fields = (
            "id",
            "url",
            "short",
        )
