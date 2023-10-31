# Generated by Django 4.2.6 on 2023-10-31 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import magoso.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to=magoso.models.path_and_resume, verbose_name='Profile Picture')),
                ('user_types', models.CharField(choices=[('instructor', 'instructor'), ('student', 'student'), ('admin', 'admin')], max_length=50)),
                ('grouping', models.CharField(choices=[('fullstack', 'fullstack'), ('frontend', 'frontend'), ('backend', 'backend')], max_length=50, null=True)),
                ('cohort', models.CharField(choices=[('cohort 4', 'cohort 4'), ('cohort 5', 'cohort 5'), ('cohort 6', 'cohort 6'), ('cohort 7', 'cohort 7'), ('cohort 8', 'cohort 8'), ('cohort 9', 'cohort 9'), ('cohort 10', 'cohort 10'), ('cohort 11', 'cohort 11'), ('cohort 12', 'cohort 12'), ('cohort 13', 'cohort 13'), ('cohort 14', 'cohort 14'), ('cohort 15', 'cohort 15'), ('cohort 16', 'cohort 16')], max_length=50)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
