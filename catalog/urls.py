from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='products_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

# urlpatterns = [
#     path('', views.home),
#     path('<int:pk>/', views.catalog, name='sub-catalog'),
#     path('<int:pk>/products', views.ProductListView, name='product-catalog'),
# ]