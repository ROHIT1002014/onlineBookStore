from django.db import models
from user.models import Profile
from book.models import Book

class Order(models.Model):

    STATUS = [('PND', 'PENDING'), ('ACT', 'ACCEPTED'), ('DND', 'DENIED'), ('CND', 'CANCELLED')]

    user = models.ForeignKey(Profile, related_name='orders', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='orders', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(choices=STATUS, default='PND', max_length=10)
    created = models.DateField(auto_now_add=True)
    order_count = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.user}: {self.date}'
