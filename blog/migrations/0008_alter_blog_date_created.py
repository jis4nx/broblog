# Generated by Django 4.0.4 on 2022-11-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_contnet_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
