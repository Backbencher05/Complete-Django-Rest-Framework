# Generated by Django 4.2.9 on 2024-01-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CarDekho_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carmodel",
            name="chachisnumber",
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name="carmodel",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
    ]
