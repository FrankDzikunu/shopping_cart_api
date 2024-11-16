from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from cart.models import CartItem


class CartAPITests(APITestCase):
    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(
            name="Test Product",
            category="Test Category",
            price=10.00,
            image_thumbnail="http://example.com/thumbnail.jpg",
            image_mobile="http://example.com/mobile.jpg",
            image_tablet="http://example.com/tablet.jpg",
            image_desktop="http://example.com/desktop.jpg",
        )

    def test_add_to_cart(self):
        response = self.client.post('/api/cart/', data={'product_id': self.product.id, 'quantity': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expect 201
        response = self.client.post('/api/cart/', data={'product_id': self.product.id, 'quantity': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expect 201
        self.assertEqual(response.data['quantity'], 2)
