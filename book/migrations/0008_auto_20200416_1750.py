# Generated by Django 3.0.5 on 2020-04-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_img',
        ),
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]