# Generated by Django 5.1.1 on 2024-10-10 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_task_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='task',
        ),
        migrations.AddField(
            model_name='timer',
            name='project',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='timer', to='app.project'),
            preserve_default=False,
        ),
    ]
