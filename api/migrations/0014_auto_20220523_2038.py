# Generated by Django 3.1 on 2022-05-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20220523_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaenc',
            name='complete_mant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='en_mantenimiento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='facturaenc',
            name='no_mantenimiento',
            field=models.BooleanField(default=False),
        ),
    ]
