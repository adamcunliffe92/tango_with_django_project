# Generated by Django 2.1.5 on 2019-02-03 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
    ]