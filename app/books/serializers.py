from rest_framework import serializers


from books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            "id",
            "title",
            "description",
            "publication_date",
            "created_at",
            "updated_at",
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("id", "user", "bio", "created_at", "updated_at")
