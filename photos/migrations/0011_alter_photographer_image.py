# Generated by Django 5.0.6 on 2024-05-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0010_alter_photographer_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photographer",
            name="image",
            field=models.ImageField(
                default="sc-logo-sm-HD.png", null=True, upload_to="photographer_profile"
            ),
        ),
    ]
