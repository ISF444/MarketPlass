from django.urls import path

from .views import get_kolobok_page

urlpatterns = [
    path('', get_kolobok_page),
]
