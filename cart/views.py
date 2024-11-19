from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import CartItem
from products.models import Product
from .serializers import CartItemSerializer

# List and Add Cart Items
class CartListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all cart items and adding new items to the cart.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_permissions(self):
        """
        Restrict POST method to authenticated users; allow read-only access for others.
        """
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle adding products to the cart with stock validation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product'].id
        quantity = serializer.validated_data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        if quantity > product.stock:
            return Response({"error": "Requested quantity exceeds available stock."}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            if cart_item.quantity + quantity > product.stock:
                return Response({"error": "Total quantity exceeds available stock."}, status=status.HTTP_400_BAD_REQUEST)
            
            cart_item.quantity += quantity
            cart_item.save()

        return Response(self.get_serializer(cart_item).data, status=status.HTTP_201_CREATED)

# Update or Delete Cart Items
class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting specific cart items.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_permissions(self):
        """
        Restrict update and delete methods to authenticated users.
        """
        return [permissions.IsAuthenticated()]

    def update(self, request, *args, **kwargs):
        """
        Custom update method to handle quantity validation.
        """
        cart_item = self.get_object()
        new_quantity = request.data.get('quantity', cart_item.quantity)

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            return Response({"error": "Quantity must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        if new_quantity <= 0:
            return Response({"error": "Quantity must be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)
        
        if new_quantity > cart_item.product.stock:
            return Response({"error": "Requested quantity exceeds available stock."}, status=status.HTTP_400_BAD_REQUEST)

        cart_item.quantity = new_quantity
        cart_item.save()
        return Response(self.get_serializer(cart_item).data, status=status.HTTP_200_OK)
