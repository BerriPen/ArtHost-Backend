# Generated by Django 5.1.3 on 2024-12-13 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0004_alter_tokenproxy_options'),
        ('main', '0010_delete_customtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('login_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('authtoken.token',),
        ),
    ]
