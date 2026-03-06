import pytest

from product.serializers import ProductSerializer
from product.factories import CategoryFactory, ProductFactory


@pytest.mark.django_db
def test_product_serializer():
    category1 = CategoryFactory()
    category2 = CategoryFactory()

    product = ProductFactory()
    product.category.add(category1, category2)

    serializer = ProductSerializer(product)

    assert serializer.data["title"] == product.title
    assert serializer.data["description"] == product.description
    assert serializer.data["price"] == product.price
    assert serializer.data["active"] == product.active
    assert len(serializer.data["category"]) == 2