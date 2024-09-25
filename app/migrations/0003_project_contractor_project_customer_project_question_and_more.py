# Generated by Django 5.1.1 on 2024-09-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_task_name_task_name_remove_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contractor',
            field=models.ManyToManyField(related_name='contractor_projects', to='app.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ManyToManyField(related_name='customer_projects', to='app.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='question',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='question_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
