from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView#, UserListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    # path('users', UserListAPIView.as_view()),
    path('<int:pk>', ProductDetailAPIView.as_view()),
]