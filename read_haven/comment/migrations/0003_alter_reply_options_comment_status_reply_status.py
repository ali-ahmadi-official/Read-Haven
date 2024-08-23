# Generated by Django 5.0.7 on 2024-07-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_publish_alter_reply_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'replies'},
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('i', 'In the review queue'), ('p', 'Published')], default='i', max_length=1),
        ),
        migrations.AddField(
            model_name='reply',
            name='status',
            field=models.CharField(choices=[('i', 'In the review queue'), ('p', 'Published')], default='i', max_length=1),
        ),
    ]
