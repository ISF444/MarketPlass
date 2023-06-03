from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    login = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.login
