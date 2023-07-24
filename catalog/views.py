from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, SubCategory, Product


def ProductListView(ListView):
    model = Product
    template_name = 'products.html'


def SubCategoryListView(ListView):
    pass


def home(request):

    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'catalog/home.html', context)


def catalog(request, pk):

    category = Category.objects.get(id=pk)
    subcategories = category.subcategory.select_related()

    context = {
        'subcategories': subcategories
    }

    return render(request, 'catalog/subcatalog.html', context)