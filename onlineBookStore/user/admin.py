from user.models import User, Profile
from django.contrib import admin

class HomeUser(admin.ModelAdmin):
    list_display = ('user', 'mobile','dob', 'address')

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Profile, HomeUser)
