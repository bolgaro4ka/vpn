# Generated by Django 5.1.2 on 2024-10-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_puser_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='puser',
            name='number_of_files',
            field=models.IntegerField(default=1, verbose_name='Кол-во профилей (.conf)'),
        ),
    ]
