# Generated by Django 4.2 on 2023-06-29 09:57

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("upload", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="firevideo",
            name="video",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location=""),
                upload_to="fire/",
            ),
        ),
    ]