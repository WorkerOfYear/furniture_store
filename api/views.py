from rest_framework import generics, permissions

from catalog.models import Product, SubCategory
from .serializers import ProductSerializer, SubCategorySerializer # UserSerializer
from .permissons import IsSuperUser
# from accounts.models import CustomUser


# class UserListAPIView(generics.ListCreateAPIView):
#     permission_classes = (IsSuperUser,)
#     # queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
