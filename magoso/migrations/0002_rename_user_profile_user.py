# Generated by Django 4.2.6 on 2023-11-02 06:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magoso', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='user',
        ),
    ]
