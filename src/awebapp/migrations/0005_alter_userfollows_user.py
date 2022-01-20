# Generated by Django 4.0.1 on 2022-01-20 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awebapp', '0004_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
