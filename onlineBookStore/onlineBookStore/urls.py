from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django_restful_admin import admin as apiAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/admin/", apiAdmin.site.urls),
    path("api/v1/", include('book.urls')),
    path("api/v1/", include('user.urls')),
    path("api/v1/", include('order.urls'))
]
