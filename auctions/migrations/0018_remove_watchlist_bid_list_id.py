# Generated by Django 3.1 on 2020-08-26 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_remove_watchlist_comment_list_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='bid_list_id',
        ),
    ]
