# Generated by Django 3.1.3 on 2024-08-17 19:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruitment', '0005_auto_20240818_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]