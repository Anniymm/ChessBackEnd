# Generated by Django 5.1.1 on 2024-09-26 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_contractor_project_contractors_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contractors',
        ),
        migrations.RemoveField(
            model_name='project',
            name='customers',
        ),
        migrations.AddField(
            model_name='project',
            name='contractors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contractor_projects', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='customers',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, related_name='customer_projects', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]