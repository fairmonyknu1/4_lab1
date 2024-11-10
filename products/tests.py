# products/tests.py

from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=10.00)

    def test_product_name(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
