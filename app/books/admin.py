from django.contrib import admin

from books import models


class BookAuthorInline(admin.TabularInline):
    model = models.BookAuthor


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date"]
    list_per_page = 10
    list_filter = ["publication_date"]
    search_fields = ["title"]
    inlines = [BookAuthorInline]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
