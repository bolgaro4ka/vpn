# Generated by Django 5.1.2 on 2024-10-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_tariff_created_at_tariff_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tariffs'),
        ),
    ]