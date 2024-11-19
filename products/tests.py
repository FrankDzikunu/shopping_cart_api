from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from cart.models import CartItem

class ProductAPITests(APITestCase):
    def setUp(self):
        """
        Create a test product that will be used in the tests.
        """
        self.product = Product.objects.create(
            name="Test Product",
            category="Test Category",
            price=10.00,
            image_thumbnail="http://example.com/thumbnail.jpg",
            image_mobile="http://example.com/mobile.jpg",
            image_tablet="http://example.com/tablet.jpg",
            image_desktop="http://example.com/desktop.jpg",
        )

    def test_get_products(self):
        """
        Test GET request for listing all products.
        """
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure the product is listed

    def test_create_product(self):
        """
        Test POST request for creating a new product.
        """
        data = {
            "name": "New Product",
            "category": "New Category",
            "price": 15.00,
            "image_thumbnail": "http://example.com/thumbnail2.jpg",
            "image_mobile": "http://example.com/mobile2.jpg",
            "image_tablet": "http://example.com/tablet2.jpg",
            "image_desktop": "http://example.com/desktop2.jpg",
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])  # Ensure the product name matches

    def test_update_product(self):
        """
        Test PUT request for updating a product.
        """
        data = {
            "name": "Updated Product",
            "category": "Updated Category",
            "price": 20.00,
            "image_thumbnail": "http://example.com/thumbnail_updated.jpg",
            "image_mobile": "http://example.com/mobile_updated.jpg",
            "image_tablet": "http://example.com/tablet_updated.jpg",
            "image_desktop": "http://example.com/desktop_updated.jpg",
        }
        response = self.client.put(f'/api/products/{self.product.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])  # Ensure the product name was updated

    def test_delete_product(self):
        """
        Test DELETE request for deleting a product.
        """
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Product should be deleted
