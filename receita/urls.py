from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_receitas.urls')),
    path('admin/', admin.site.urls),
]

