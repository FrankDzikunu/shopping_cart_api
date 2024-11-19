from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# List and Create Products
class ProductListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all products and creating a new product.
    Supports filtering products by category or price range using query parameters.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally filter products by category, minimum price, or maximum price.
        Query parameters:
        - category: Filter products by category (case-insensitive, partial match).
        - min_price: Filter products with price >= min_price.
        - max_price: Filter products with price <= max_price.
        """
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)

        if category:
            queryset = queryset.filter(category__icontains=category)
        if min_price:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                pass  # Invalid min_price input; ignore this filter
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass  # Invalid max_price input; ignore this filter

        return queryset

    def get_permissions(self):
        """
        Restrict POST method to admin users; allow read-only access for others.
        """
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle stock validation before adding a product.
        """
        data = request.data
        if 'stock' in data and int(data['stock']) < 0:
            return Response({"error": "Stock cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

# Retrieve, Update, and Delete Products
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific product by ID.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        """
        Restrict update and delete methods to admin users; allow read-only access for others.
        """
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def update(self, request, *args, **kwargs):
        """
        Custom update method to validate stock.
        """
        data = request.data
        if 'stock' in data and int(data['stock']) < 0:
            return Response({"error": "Stock cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().update(request, *args, **kwargs)
