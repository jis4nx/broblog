# Generated by Django 4.0.4 on 2022-11-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]