import pytest

from product.serializers import CategorySerializer
from product.factories import CategoryFactory


@pytest.mark.django_db
def test_category_serializer():
    category = CategoryFactory()

    serializer = CategorySerializer(category)

    assert serializer.data["title"] == category.title
    assert serializer.data["slug"] == category.slug
    assert serializer.data["description"] == category.description
    assert serializer.data["active"] == category.active