from django.shortcuts import render

from .models import Category, SubCategory, Product


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