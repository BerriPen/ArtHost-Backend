# Generated by Django 5.1.3 on 2024-12-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_customtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='login_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
