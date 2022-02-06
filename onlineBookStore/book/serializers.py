from rest_framework import serializers
from book.models import Book
from rest_framework.validators import UniqueTogetherValidator

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('name', 'author', 'price', 'edition', 'isbn',)
            )
        ]
