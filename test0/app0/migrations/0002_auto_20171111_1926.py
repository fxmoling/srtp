# # -*- coding: utf-8 -*-
# # Generated by Django 1.11 on 2017-11-11 11:26
# from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0001_initial'),
    ]
#
#     operations = [
#         migrations.CreateModel(
#             name='PaperMetaInfo',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('title', models.CharField(max_length=32)),
#                 ('summary', models.CharField(max_length=400)),
#                 ('filepath', models.FileField(upload_to='./pdf')),
#             ],
#         ),
#         migrations.CreateModel(
#             name='Ids',
#             fields=[
#                 ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
#             ],
#         ),
#         migrations.CreateModel(
#             name='UserMetaInfo',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('username', models.CharField(max_length=20)),
#                 ('password', models.CharField(default='', max_length=32)),
#             ],
#         ),
#         migrations.DeleteModel(
#             name='Plane',
#         ),
#     ]
