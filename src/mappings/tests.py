from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import URLMapping


class URLMappingTests(TestCase):
    def test_create_urlmapping_unique(self):
        """Testuje unikalność shortu"""

        # Utworzenie pierwszej instancji
        urlmapping = URLMapping.objects.create(url="https://www.example.com")

        self.assertIsNotNone(urlmapping.short)
        self.assertRegex(urlmapping.short, r"^[a-zA-Z]{8}$")

        # Utworzenie drugiej instancji z tym samym URL
        urlmapping2 = URLMapping.objects.create(url="https://www.example.com")

        self.assertIsNotNone(urlmapping2.short)
        self.assertRegex(urlmapping2.short, r"^[a-zA-Z]{8}$")
        self.assertNotEqual(urlmapping.short, urlmapping2.short)

    def test_create_remove_urlmapping(self):
        """Testuje tworzenie i usuwanie URLMapping."""

        urlmapping = URLMapping.objects.create(url="https://www.example.com")

        self.assertIsNotNone(urlmapping.short)
        self.assertRegex(urlmapping.short, r"^[a-zA-Z]{8}$")

        urlmapping.delete()

        self.assertIsNone(URLMapping.objects.filter(short=urlmapping.short).first())

    def test_empty_url(self):
        """Testuje tworzenie URLMapping z pustym URL."""

        with self.assertRaises(ValidationError):
            URLMapping.objects.create(url="")

    def test_invalid_url(self):
        """Testuje tworzenie URLMapping z nieprawidłowym URL."""

        with self.assertRaises(ValidationError):
            URLMapping.objects.create(url="invalid-url")
