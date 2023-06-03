from django.contrib import admin

# Register your models here.
from .models import Product, Category, Person

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Person)
