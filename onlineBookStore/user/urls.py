from django.urls import path, include
# from menu.views import CategoryList, ItemList
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'categories', CategoryList, basename="category")

urlpatterns = router.urls
