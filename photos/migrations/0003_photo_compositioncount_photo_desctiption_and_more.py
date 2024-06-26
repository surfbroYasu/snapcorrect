# Generated by Django 5.0.6 on 2024-05-17 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0002_category_alter_photo_image_photo_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="CompositionCount",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="photo",
            name="desctiption",
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name="Photographer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("base_location", models.CharField(max_length=255, null=True)),
                ("introduction", models.TextField(max_length=1000, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photographer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="photo",
            name="Photographer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="photos.photographer",
            ),
            preserve_default=False,
        ),
    ]
