# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-20 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('banner', models.FileField(blank=True, upload_to=b'poko_image')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('serial_number', models.IntegerField(default=0)),
                ('product_image', models.FileField(blank=True, upload_to=b'images/productimages')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Brands')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='SoldItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('type', models.CharField(default=None, max_length=100)),
                ('image', models.FileField(blank=True, upload_to=b'poko_image')),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('pass_word', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='usercart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Users'),
        ),
        migrations.AddField(
            model_name='solditems',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Users'),
        ),
        migrations.AddField(
            model_name='categories',
            name='store_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apiApp.Store'),
        ),
    ]
