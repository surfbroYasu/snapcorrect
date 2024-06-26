# Generated by Django 5.0.6 on 2024-05-17 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0003_photo_compositioncount_photo_desctiption_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="Photographer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="photos.photographer",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(default="noImage.png", upload_to="images/"),
        ),
    ]
