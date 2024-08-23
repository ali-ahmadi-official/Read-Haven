# Generated by Django 5.0.7 on 2024-08-03 14:04

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name', unique=True),
        ),
    ]
