# Generated by Django 5.0.7 on 2024-07-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_remove_gallery_language_remove_gallery_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="title",
            field=models.CharField(default="None", max_length=255),
        ),
        migrations.DeleteModel(
            name="GalleryTranslation",
        ),
    ]
