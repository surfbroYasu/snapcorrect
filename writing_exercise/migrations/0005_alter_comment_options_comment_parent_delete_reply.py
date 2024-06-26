# Generated by Django 5.0.6 on 2024-05-23 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("writing_exercise", "0004_alter_reply_reply_to"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-datetime"]},
        ),
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="writing_exercise.comment",
            ),
        ),
        migrations.DeleteModel(
            name="Reply",
        ),
    ]
