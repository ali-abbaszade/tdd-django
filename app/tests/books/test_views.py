from django.contrib.auth import get_user_model
from django.urls import reverse
import pytest

from books.models import Book, Author


@pytest.mark.django_db
def test_add_book(client):
    user = get_user_model().objects.create_user(
        username="user", password="testpassword"
    )
    author = Author.objects.create(user=user)
    books = Book.objects.all()
    assert len(books) == 0

    url = reverse("book-list")
    resp = client.post(
        url,
        {
            "authors": [{"author": author.id}],
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


@pytest.mark.django_db
def test_get_single_book(client):
    book = Book.objects.create(
        title="a", description="abc", publication_date="2020-01-03"
    )

    url = reverse("book-detail", args=[book.id])
    resp = client.get(url)

    assert resp.status_code == 200
    assert resp.data["title"] == "a"


@pytest.mark.django_db
def test_get_single_book_invalid_id(client):
    resp = client.get("api/books/not-id/")

    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_single_author(client):
    user = get_user_model().objects.create_user(
        username="user", password="testpassword"
    )
    author = Author.objects.create(user=user)

    url = reverse("author-detail", args=[author.id])
    resp = client.get(url)

    assert resp.status_code == 200
    assert resp.data["user"] == user.id


@pytest.mark.django_db
def test_get_author_invalid_id(client):
    resp = client.get("api/authors/not-id/")

    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_books(client):
    book_1 = Book.objects.create(title="Book 1", publication_date="2020-10-02")
    book_2 = Book.objects.create(title="Book 2", publication_date="2021-11-03")

    url = reverse("book-list")
    resp = client.get(url)

    assert resp.status_code == 200
    assert resp.data[0]["title"] == book_1.title
    assert resp.data[1]["title"] == book_2.title


@pytest.mark.django_db
def test_get_all_authors(client):
    user_1 = get_user_model().objects.create_user(
        username="user_one", password="testpassword"
    )
    user_2 = get_user_model().objects.create_user(
        username="user_two", password="testpassword"
    )
    author_1 = Author.objects.create(user=user_1)
    author_2 = Author.objects.create(user=user_2)

    url = reverse("author-list")
    resp = client.get(url)

    assert resp.status_code == 200
    assert resp.data[0]["user"] == user_1.id
    assert resp.data[1]["user"] == user_2.id
