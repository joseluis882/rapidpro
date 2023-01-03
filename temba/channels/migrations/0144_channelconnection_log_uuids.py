# Generated by Django 4.0.7 on 2022-09-05 16:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0143_channellog_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="channelconnection",
            name="log_uuids",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), null=True, size=None),
        ),
        migrations.AddField(
            model_name="channelevent",
            name="log_uuids",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), null=True, size=None),
        ),
    ]