from django.urls import path

from .views import get_page_all_forms, get_people

urlpatterns = [
    path('', get_page_all_forms, name='forms_page'),
    path("people/", get_people),

]
