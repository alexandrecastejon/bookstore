from django.test import TestCase

from product.serializers import ProductSerializer
from product.factories import CategoryFactory, ProductFactory


class TestProductSerializer(TestCase):
    def test_product_serializer(self):
        category1 = CategoryFactory()
        category2 = CategoryFactory()

        product = ProductFactory()
        product.category.add(category1, category2)

        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data["title"], product.title)
        self.assertEqual(serializer.data["description"], product.description)
        self.assertEqual(serializer.data["price"], product.price)
        self.assertEqual(serializer.data["active"], product.active)
        self.assertEqual(len(serializer.data["category"]), 2)