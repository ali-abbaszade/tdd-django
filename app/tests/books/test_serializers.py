from django.contrib.auth import get_user_model

import pytest
from books import serializers


User = get_user_model()


def test_valid_book_serializer():
    valid_data = {
        "title": "Sample Book",
        "description": "Sample description.",
        "publication_date": "2025-01-20",
    }
    serializer = serializers.BookSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.data == valid_data
    assert serializer.errors == {}


def test_invalid_book_serializer():
    invalid_data = {
        "title": "Sample Book",
        "description": "Sample description.",
    }
    serializer = serializers.BookSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.data == invalid_data
    assert serializer.errors == {"publication_date": ["This field is required."]}


@pytest.mark.django_db
def test_valid_author_serializer():
    user = User.objects.create_user(username="a", password="123")
    valid_data = {"user": user.id, "bio": "foo"}
    serializer = serializers.AuthorSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.data == valid_data
    assert serializer.errors == {}


def test_invalid_author_serializer():
    invalid_data = {
        "bio": "foo",
    }
    serializer = serializers.AuthorSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.data == invalid_data
    assert serializer.errors == {"user": ["This field is required."]}
