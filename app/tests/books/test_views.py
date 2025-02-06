from django.contrib.auth import get_user_model
from django.urls import reverse
import pytest

from books.models import Book, Author


@pytest.mark.django_db
def test_add_book(client):
    books = Book.objects.all()
    assert len(books) == 0

    url = reverse("book-list")
    resp = client.post(
        url,
        {
            "title": "book title",
            "description": "a description",
            "publication_date": "2020-10-20",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "book title"

    books = Book.objects.all()
    assert len(books) == 1


@pytest.mark.django_db
def test_add_book_invalid_payload(client):
    books = Book.objects.all()
    assert len(books) == 0

    url = reverse("book-list")
    resp = client.post(url, {}, content_type="application/json")

    assert resp.status_code == 400

    books = Book.objects.all()
    assert len(books) == 0


@pytest.mark.django_db
def test_add_author(client):
    user = get_user_model().objects.create_user(
        username="user", password="testpassword"
    )
    authors = Author.objects.all()
    assert len(authors) == 0

    url = reverse("author-list")
    resp = client.post(
        url,
        {
            "user": user.id,
            "bio": "test bio",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["user"] == user.id

    authors = Author.objects.all()
    assert len(authors) == 1


@pytest.mark.django_db
def test_add_author_invalid_payload(client):
    authors = Author.objects.all()
    assert len(authors) == 0

    url = reverse("author-list")
    resp = client.post(url, {}, content_type="application/json")

    assert resp.status_code == 400

    authors = Author.objects.all()
    assert len(authors) == 0
