# Generated by Django 3.2.9 on 2022-01-16 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_integration_client_org_related'),
    ]

    operations = [
        migrations.RenameField(
            model_name='integration',
            old_name='client_org_related',
            new_name='client_related',
        ),
    ]