import logging

from book.models import Book
from django_filters.rest_framework import FilterSet

logger = logging.getLogger(__name__)

class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['name', 'author']
