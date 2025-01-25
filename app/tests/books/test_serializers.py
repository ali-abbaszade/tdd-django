from django.contrib.auth import get_user_model
from django.utils import timezone

from books import serializers


User = get_user_model()


def test_valid_book_serializer():
    valid_data = {
        "title": "Sample Book",
        "description": "Sample description.",
        "publication_date": timezone.datetime(2025, 1, 20).date(),
    }
    serializer = serializers.BookSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.error == {}


def test_invalid_book_serializer():
    invalid_data = {
        "title": "Sample Book",
        "description": "Sample description.",
    }
    serializer = serializers.BookSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_data
    assert serializer.errors == {"publication_date": ["This field is required."]}


def test_valid_author_serializer():
    user = User.objects.create_user(username="a", password="123")
    valid_data = {"user": user, "bio": "foo"}
    serializer = serializers.AuthorSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_data
    assert serializer.data == valid_data
    assert serializer.error == {}


def test_invalid_author_serializer():
    invalid_data = {
        "bio": "foo",
    }
    serializer = serializers.AuthorSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_data
    assert serializer.errors == {"user": ["This field is required."]}
