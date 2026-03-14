from django.test import TestCase

from order.serializers import OrderSerializer
from order.factories import OrderFactory
from product.factories import ProductFactory


class TestOrderSerializer(TestCase):
    def test_order_serializer_total(self):
        product1 = ProductFactory(price=100)
        product2 = ProductFactory(price=200)

        order = OrderFactory()
        order.product.add(product1, product2)

        serializer = OrderSerializer(order)

        self.assertEqual(serializer.data["total"], 300)
        self.assertEqual(len(serializer.data["product"]), 2)