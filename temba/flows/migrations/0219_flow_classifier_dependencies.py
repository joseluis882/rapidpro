# Generated by Django 2.2.4 on 2019-10-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0001_initial'),
        ('flows', '0218_auto_20190813_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='flow',
            name='classifier_dependencies',
            field=models.ManyToManyField(related_name='dependent_flows', to='classifiers.Classifier'),
        ),
    ]
