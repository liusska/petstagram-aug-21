# Generated by Django 3.1.3 on 2021-09-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
    ]