from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product
from cart.models import CartItem

class CartAPITests(APITestCase):
    def setUp(self):
        """
        Create a test product and an initial cart item for testing.
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
        self.cart_item = CartItem.objects.create(product=self.product, quantity=1)

    def test_add_to_cart(self):
        """
        Test POST request to add a product to the cart.
        """
        response = self.client.post('/api/cart/', data={'product_id': self.product.id, 'quantity': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Product added successfully
        self.assertEqual(response.data['quantity'], 1)

        # Add more of the same product to the cart
        response = self.client.post('/api/cart/', data={'product_id': self.product.id, 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], 3)  # Quantity should be updated

    def test_get_cart_items(self):
        """
        Test GET request to list all cart items.
        """
        response = self.client.get('/api/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure the cart item is listed

    def test_remove_cart_item(self):
        """
        Test DELETE request to remove a cart item.
        """
        response = self.client.delete(f'/api/cart/{self.cart_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Item deleted
