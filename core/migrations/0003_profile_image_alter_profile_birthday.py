# Generated by Django 5.0.6 on 2024-06-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_school_profile_is_teacher_profile_organization"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="sc-logo-sm-HD.png", null=True, upload_to="user_profile/"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
    ]
