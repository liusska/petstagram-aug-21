# Generated by Django 3.1.3 on 2022-01-07 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0004_pet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
    ]
