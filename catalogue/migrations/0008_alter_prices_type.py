# Generated by Django 5.0.6 on 2024-11-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_rename_price_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='type',
            field=models.CharField(max_length=30),
        ),
    ]