# Generated by Django 3.1.3 on 2024-08-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0011_auto_20240823_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.IntegerField(),
        ),
    ]
