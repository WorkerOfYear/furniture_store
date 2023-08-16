from django.test import TestCase
from .models import Product, Category, SubCategory, Discount


# class ModelsTest(TestCase):

#     def test_create_Category(self):
#         Category.objects.create(
#             name='test_category',
#         ).save()

#         print(Category.objects.all())
#         expected_category_name = Category.objects.get(id=1).name

#         self.assertEqual(expected_category_name, 'test_category')


#     def test_create_SubCategory(self):
#         print(Category.objects.all())
#         SubCategory.objects.create(
#             name='test_subcategory',
#             # category=Category.objects.get(id=1),
#         ).save()

#         expected_subcategory_name = SubCategory.objects.get(id=1).name
#         expected_subcategory_category_name = SubCategory.objects.get(id=1).category.name

#         self.assertEqual(expected_subcategory_name, 'test_subcategory')
#         self.assertEqual(expected_subcategory_category_name, 'test_category')




    # def createDiscount(self):
    #     Discount.objects.create(
    #         name='test_subcategory',
    #         percent=100.00
    #     ).save()

    # def createProduct(self):
    #     Product.objects.create(
    #         name='test_name',
    #         description='test_description',
    #         price=10000,

    #         category=Category.objects.get(id=1),
    #         subcategory=SubCategory.objects.get(id=1),
    #         discount=Discount.objects.get(id=1),
    #     ).save()

    # def test_product(self):
    #     product = Product.objects.get(id=1)
    #     expected_object_name = f'{product.name}'
    #     expected_object_description = f'{product.description}'
    #     expected_object_price = f'{product.price}'
    #     self.assertEqual(expected_object_name, 'test_name')
    #     self.assertEqual(expected_object_description, 'test_description')
    #     self.assertEqual(expected_object_price, '10000')
