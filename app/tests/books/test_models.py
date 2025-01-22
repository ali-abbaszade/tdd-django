from django.utils import timezone
from django.contrib.auth import get_user_model

import pytest

from books import models


@pytest.mark.django_db
def test_book_model():
    specific_date = timezone.datetime(2025, 1, 10).date()
    book = models.Book.objects.create(
        title="a", description="abc", publication_data=specific_date
    )
    assert book.title == "a"
    assert book.description == "abc"
    assert book.publication_date == specific_date
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title


@pytest.mark.django_db
def test_author_model():
    user = get_user_model().objects.create(
        username="testuser",
        password="pass123",
        first_name="John",
        last_name="Doe",
        email="author@email.com",
    )
    author = models.Author.objects.create(user=user, bio="abc")
    assert author.user.first_name == "John"
    assert author.user.email == "author@email.com"
    assert author.user.username == "testuser"
    assert author.bio == "abc"
    assert created_at
    assert updated_at
    assert str(author) == "John Doe"


@pytest.mark.django_db
def test_book_author_model():
    book = models.Book.objects.create(
        title="a", description="abc", publication_data=timezone.now().date()
    )
    user = get_user_model().objects.create(username="testuser", password="password123")
    author = models.Author.objects.create(user=user)
    book_author = models.bookAuthor.objects.create(book=book, author=author)

    assert book_author.book.id == book.id
    assert book_author.author.id == author.id


@pytest.mark.django_db
def test_book_author_unique_constraint():
    book = models.Book.objects.create(
        title="a", description="abc", publication_data=timezone.now().date()
    )
    user = get_user_model().objects.create(username="testuser", password="password123")
    author = models.Author.objects.create(user=user)
    models.bookAuthor.objects.create(book=book, author=author)

    with pytest.raises(Exception) as excinfo:
        models.bookAuthor.objects.create(book=book, author=author)

    assert "unique constraint" in str(excinfo)
