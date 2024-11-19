from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product',
        label="Product ID",
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'total_price']
        read_only_fields = ['total_price']

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        """Calculate total price for a cart item."""
        return obj.get_total_price()
