from rest_framework import generics
from catalog.models import Product, SubCategory
from .serializers import ProductSerializer, SubCategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
