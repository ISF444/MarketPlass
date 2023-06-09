from django.db import models


class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name