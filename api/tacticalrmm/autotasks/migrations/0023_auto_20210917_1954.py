# Generated by Django 3.2.6 on 2021-09-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autotasks", "0022_automatedtask_collector_all_output"),
    ]

    operations = [
        migrations.AlterField(
            model_name="automatedtask",
            name="created_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="automatedtask",
            name="modified_by",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
