# Generated by Django 4.2 on 2023-05-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_model', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
