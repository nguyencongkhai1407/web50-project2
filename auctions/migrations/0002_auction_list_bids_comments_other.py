# Generated by Django 3.1 on 2020-08-20 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_list', models.CharField(default='', max_length=64)),
                ('starting_bid', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=64)),
                ('url', models.CharField(default='', max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_list')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='', max_length=64)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_list')),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bids', models.IntegerField(default=0)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_list')),
            ],
        ),
    ]
