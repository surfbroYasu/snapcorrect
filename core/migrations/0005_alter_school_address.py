# Generated by Django 5.0.6 on 2024-06-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_school_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="address",
            field=models.TextField(blank=True, max_length=125, null=True),
        ),
    ]
