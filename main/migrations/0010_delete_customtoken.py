# Generated by Django 5.1.3 on 2024-12-13 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_customtoken_usertoken_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomToken',
        ),
    ]
