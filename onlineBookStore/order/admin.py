from order.models import Order
from django.contrib import admin


class HomeOrder(admin.ModelAdmin):
    list_display = ('user', 'book', 'date', 'status', 'created',)


admin.site.register(Order, HomeOrder)
