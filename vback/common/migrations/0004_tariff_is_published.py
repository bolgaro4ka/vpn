# Generated by Django 5.1.2 on 2024-10-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_tariff_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
