# Generated by Django 3.2.9 on 2022-01-19 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0005_rename_client_org_related_integration_client_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='integration',
            name='agent_related',
            field=models.BooleanField(default=False),
        ),
    ]
