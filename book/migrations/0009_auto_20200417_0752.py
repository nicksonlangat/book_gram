# Generated by Django 3.0.5 on 2020-04-17 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20200416_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookreviews',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True),
        ),
    ]
