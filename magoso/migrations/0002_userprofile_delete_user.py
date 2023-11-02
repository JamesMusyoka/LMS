# Generated by Django 4.2.6 on 2023-11-02 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magoso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100)),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to='Images/', verbose_name='Profile Picture')),
                ('user_types', models.CharField(choices=[('instructor', 'instructor'), ('student', 'student'), ('admin', 'admin')], max_length=50)),
                ('grouping', models.CharField(choices=[('fullstack', 'fullstack'), ('frontend', 'frontend'), ('backend', 'backend')], max_length=50, null=True)),
                ('cohort', models.CharField(choices=[('cohort 4', 'cohort 4'), ('cohort 5', 'cohort 5'), ('cohort 6', 'cohort 6'), ('cohort 7', 'cohort 7'), ('cohort 8', 'cohort 8'), ('cohort 9', 'cohort 9'), ('cohort 10', 'cohort 10'), ('cohort 11', 'cohort 11'), ('cohort 12', 'cohort 12'), ('cohort 13', 'cohort 13'), ('cohort 14', 'cohort 14'), ('cohort 15', 'cohort 15'), ('cohort 16', 'cohort 16')], max_length=50)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]