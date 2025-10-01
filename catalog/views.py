from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to Product Catalog API 🚀</h1><p>Use <a href='/api/products/'>/api/products/</a> to access the API.</p>")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
