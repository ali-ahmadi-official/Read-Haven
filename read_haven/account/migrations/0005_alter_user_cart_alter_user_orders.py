# Generated by Django 5.0.7 on 2024-08-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_cart'),
        ('book', '0014_rename_get_full_name_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='cart', to='book.book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, related_name='orders', to='book.book'),
        ),
    ]
