# Generated by Django 5.0.7 on 2024-07-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_gallery_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("ru", "Russian")],
                default="en",
                max_length=10,
            ),
        ),
    ]
