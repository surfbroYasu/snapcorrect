# Generated by Django 5.0.6 on 2024-05-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0008_photographer_artist_name_alter_photo_photographer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photographer",
            name="image",
            field=models.ImageField(
                default="media/images/sc-logo-sm-HD.png", null=True, upload_to=""
            ),
        ),
    ]
