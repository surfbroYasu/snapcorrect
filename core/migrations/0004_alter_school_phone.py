# Generated by Django 5.0.6 on 2024-06-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_profile_image_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="phone",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]