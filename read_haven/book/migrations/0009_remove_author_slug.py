# Generated by Django 5.0.7 on 2024-08-03 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]
