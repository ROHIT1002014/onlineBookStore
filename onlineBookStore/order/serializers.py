from rest_framework import serializers
from order.models import Order
from book.models import Book
from user.models import Profile
from book.serializers import BookSerializer
from user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        book = BookSerializer(Book.objects.get(pk=ret['book'])).data
        user = UserSerializer(Profile.objects.get(pk=ret['user'])).data
        ret['user'] = book
        ret['book'] = user
        return ret
