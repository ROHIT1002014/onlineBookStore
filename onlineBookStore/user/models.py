from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile',
        on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=13, blank=True, default='')
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30, blank=True, default='')
    user_image = models.ImageField(
        upload_to='profile_img', blank=True, default="profile_img/default.png")
    favorite_books = models.ManyToManyField(
        Book, related_name='user_fav_books')
    reading_list = models.ManyToManyField(
        Book, related_name='user_reading_list')

    def __str__(self):
        return self.user.username
