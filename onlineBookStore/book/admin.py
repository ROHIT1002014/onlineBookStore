from book.models import Book
from django.contrib import admin

class HomeBook(admin.ModelAdmin):
    list_display = ('name', 'author','price', 'edition', 'isbn', 'timestamp')

admin.site.register(Book, HomeBook)
