# Generated by Django 3.1 on 2020-08-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_list_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='url',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
