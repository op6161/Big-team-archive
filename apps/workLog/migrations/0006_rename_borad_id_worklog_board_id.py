# Generated by Django 4.2.2 on 2023-06-13 14:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("workLog", "0005_alter_worklog_end_alter_worklog_start"),
    ]

    operations = [
        migrations.RenameField(
            model_name="worklog",
            old_name="borad_id",
            new_name="board_id",
        ),
    ]
