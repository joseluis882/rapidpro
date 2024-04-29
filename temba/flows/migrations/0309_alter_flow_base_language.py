# Generated by Django 4.0.8 on 2023-01-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flows", "0308_alter_flow_base_language_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flow",
            name="base_language",
            field=models.CharField(
                default="und",
                help_text="The authoring language, additional languages can be added later.",
                max_length=4,
            ),
        ),
    ]
