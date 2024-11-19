from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'price',
            'image_thumbnail',
            'image_mobile',
            'image_tablet',
            'image_desktop',
            'stock',
            'description',
            'is_in_stock',
        ]
        read_only_fields = ['is_in_stock']
