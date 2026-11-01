from django.test import TestCase
from rest_framework.test import APIClient

from mappings.models import URLMapping

TEST_URL = "https://www.example.com"


class URLMappingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_url_mapping(self):
        """Prosty test tworzenia mapowania URL"""

        response = self.client.post("/api/", data={"url": TEST_URL}, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertRegex(response.json()["short"], r"^[a-zA-Z]{8}$")

    def test_get_url_mapping(self):
        """Prosty test pobierania mapowania URL po utworzeniu"""

        response = self.client.post("/api/", data={"url": TEST_URL}, format="json")

        self.assertEqual(response.status_code, 201)

        response2 = self.client.get(f"/api/{response.json()['short']}/", format="json")

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json()["url"], TEST_URL)

    def test_invalid_url(self):
        """Test nieprawidłowego URL"""

        response = self.client.post("/api/", data={"url": "invalid-url"}, format="json")

        self.assertEqual(response.status_code, 400)

    def test_empty_url(self):
        """Test pustego URL"""

        response = self.client.post("/api/", data={"url": ""}, format="json")

        self.assertEqual(response.status_code, 400)

    def test_nonexistent_url_mapping(self):
        """Test pobierania nieistniejącego mapowania URL"""

        # Nie mamy metod usuwania mapowań więc trzeba usunąć wszystkie na
        # wszelki wypadek
        URLMapping.objects.all().delete()

        response = self.client.get("/api/kkkkkkkk/", format="json")

        self.assertEqual(response.status_code, 404)
