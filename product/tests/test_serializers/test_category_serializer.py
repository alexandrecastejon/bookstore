from django.test import TestCase

from product.serializers import CategorySerializer
from product.factories import CategoryFactory


class TestCategorySerializer(TestCase):
    def test_category_serializer(self):
        category = CategoryFactory()

        serializer = CategorySerializer(category)

        self.assertEqual(serializer.data["title"], category.title)
        self.assertEqual(serializer.data["slug"], category.slug)
        self.assertEqual(serializer.data["description"], category.description)
        self.assertEqual(serializer.data["active"], category.active)