from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductAPITests(APITestCase):
    def setUp(self):
        Product.objects.create(
            name="Test Product",
            category="Test Category",
            price=10.00,
            image_thumbnail="http://example.com/thumbnail.jpg",
            image_mobile="http://example.com/mobile.jpg",
            image_tablet="http://example.com/tablet.jpg",
            image_desktop="http://example.com/desktop.jpg",
        )

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
