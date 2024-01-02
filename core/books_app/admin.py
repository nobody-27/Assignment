from django.contrib import admin
from books_app.models import Book

# Register your models here.


@admin.register(Book)
class Booksadmin(admin.ModelAdmin):
    list_display = ['title','author','published_date']
