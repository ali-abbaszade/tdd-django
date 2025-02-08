from rest_framework import serializers


from books import models


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookAuthor
        fields = ("author",)


class BookSerializer(serializers.ModelSerializer):
    authors = BookAuthorSerializer(many=True)

    class Meta:
        model = models.Book
        fields = (
            "id",
            "authors",
            "title",
            "description",
            "publication_date",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        authors = validated_data.pop("authors")
        book = models.Book.objects.create(**validated_data)
        for author in authors:
            models.BookAuthor.objects.create(book=book, **author)
        return book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "user", "bio", "created_at", "updated_at")
