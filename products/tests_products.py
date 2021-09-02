from django.test import TestCase
from products.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="Одежда")

        self.product_1 = Product.objects.create(name="Худи",
                                                category=category,
                                                price=1999.5,
                                                quantity=150)

        self.product_2 = Product.objects.create(name="Куртка",
                                                category=category,
                                                price=2998.1,
                                                quantity=125,
                                                is_active=False)

        self.product_3 = Product.objects.create(name="Брюки",
                                                category=category,
                                                price=998.1,
                                                quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="Худи")
        product_2 = Product.objects.get(name="Куртка")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="Худи")
        product_2 = Product.objects.get(name="Куртка")
        self.assertEqual(str(product_1), 'Худи | Одежда')
        self.assertEqual(str(product_2), 'Куртка | Одежда')

    # def test_product_get_items(self):
    #     product_1 = Product.objects.get(name="Худи")
    #     product_3 = Product.objects.get(name="Брюки")
    #     products = product_1.get_items()
    #
    #     self.assertEqual(list(products), [product_1, product_3])
