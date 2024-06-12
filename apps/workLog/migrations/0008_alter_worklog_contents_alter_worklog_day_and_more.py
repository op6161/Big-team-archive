# Generated by Django 4.2.2 on 2023-06-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workLog", "0007_alter_worklog_end_alter_worklog_in_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worklog",
            name="contents",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="day",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="end",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="in_time",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="out_time",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="start",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="worklog",
            name="work_type",
            field=models.CharField(max_length=50),
        ),
    ]
