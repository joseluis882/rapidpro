# Generated by Django 4.0.7 on 2022-09-08 15:02

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0144_channelconnection_log_uuids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channellog",
            name="elapsed_ms",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="channellog",
            name="log_type",
            field=models.CharField(
                choices=[
                    ("unknown", "Other Event"),
                    ("msg_send", "Message Send"),
                    ("msg_status", "Message Status"),
                    ("msg_receive", "Message Receive"),
                    ("event_receive", "Event Receive"),
                    ("ivr_start", "IVR Start"),
                    ("ivr_incoming", "IVR Incoming"),
                    ("ivr_callback", "IVR Callback"),
                    ("ivr_status", "IVR Status"),
                    ("ivr_hangup", "IVR Hangup"),
                    ("token_refresh", "Token Refresh"),
                    ("page_subscribe", "Page Subscribe"),
                ],
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="channellog",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
