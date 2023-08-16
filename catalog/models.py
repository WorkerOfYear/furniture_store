from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', args=[self.slug])

    class Meta:
        ordering: ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return str(self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategory')
    photo = models.ImageField(null=True, blank=True, default='default.png')

    def __str__(self) -> str:
        return str(self.name)


# class Brand(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return str(self.name)


class Discount(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    subcategory = models.ManyToManyField(SubCategory, blank=True)
    discount = models.ManyToManyField(Discount, blank=True)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self) -> str:
        return str(self.name)
