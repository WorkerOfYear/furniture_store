from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    photo = models.ImageField(null=True, default='default.png')

    def __str__(self) -> str:
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class Discount(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    percnet = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(SubCategory)
    discount = models.ManyToManyField(Discount)

    def __str__(self) -> str:
        return str(self.name)
