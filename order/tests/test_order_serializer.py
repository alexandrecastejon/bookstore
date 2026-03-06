import pytest

from order.serializers import OrderSerializer
from order.factories import OrderFactory
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_serializer_total():
    product1 = ProductFactory(price=100)
    product2 = ProductFactory(price=200)

    order = OrderFactory()
    order.product.add(product1, product2)

    serializer = OrderSerializer(order)

    assert serializer.data["total"] == 300
    assert len(serializer.data["product"]) == 2