# Generated by Django 5.0.7 on 2024-07-28 08:33

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('cover_image', models.ImageField(default='default/default.png', upload_to='book_photos/')),
                ('book_publish_time', models.IntegerField(help_text='Please enter the publication year (e.g., 2024)')),
                ('availability', models.CharField(choices=[('e', 'Existent book'), ('n', 'Non-existent book')], default='e', help_text="If the 'Non-existent book' option is selected, 'Out Of Stock' will be displayed in the product price section.", max_length=1)),
                ('price', models.CharField(help_text='based on US dollars', max_length=20)),
                ('type_of_book', models.CharField(choices=[('p', 'Paper book'), ('e', 'Electronic book')], default='p', max_length=1)),
                ('status', models.CharField(choices=[('i', 'In the review queue'), ('p', 'Published')], default='i', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_author', to='book.author')),
                ('category', models.ManyToManyField(related_name='books_category', to='book.category')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='book_photos/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='book.book')),
            ],
        ),
    ]
