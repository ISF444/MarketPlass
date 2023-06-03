from django.urls import path

from .views import get_products, get_all_product_category
app = 'lesson_model'
urlpatterns = [
    path('', get_products, name='all'),
    path('category/<int:id>', get_all_product_category, name="johan"),
]
