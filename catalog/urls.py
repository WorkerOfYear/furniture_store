from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('<int:pk>/', views.catalog, name='sub-catalog'),
    path('<int:pk>/products', views.ProductListView, name='product-catalog'),
]