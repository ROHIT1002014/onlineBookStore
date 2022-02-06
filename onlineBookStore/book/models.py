from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField()
    edition = models.CharField(max_length=15, blank='', null=True)
    isbn = models.CharField(blank='', max_length=20)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    time = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='books_img',
                              blank=True, default="books_img/default.png")

    def __str__(self):
        return self.name
