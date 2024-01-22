from django.contrib import admin
from django.urls import path

from main.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='hone'),
    path('about/', about, name='about')
]
