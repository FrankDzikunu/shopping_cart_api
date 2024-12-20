from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# List and Create Products
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
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
                pass  
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass  

        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        data = request.data
        if 'stock' in data and int(data['stock']) < 0:
            return Response({"error": "Stock cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

# Retrieve, Update, and Delete Products
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def update(self, request, *args, **kwargs):
        data = request.data
        if 'stock' in data and int(data['stock']) < 0:
            return Response({"error": "Stock cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().update(request, *args, **kwargs)
