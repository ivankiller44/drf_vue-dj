# Generated by Django 3.1 on 2022-03-02 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_facturadet_facturaenc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaenc',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=100),
        ),
    ]
