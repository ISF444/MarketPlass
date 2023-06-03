from django.urls import path

from .views import get_kol_0

urlpatterns = [
    path('', get_kol_0),
]