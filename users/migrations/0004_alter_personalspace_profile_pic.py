# Generated by Django 5.1.1 on 2024-10-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_personalspace_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalspace',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile/profile_pic.jpg', upload_to='media/profile'),
        ),
    ]
