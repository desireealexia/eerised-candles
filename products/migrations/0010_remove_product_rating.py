# Generated by Django 4.2.20 on 2025-04-13 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
