# Generated by Django 3.2.8 on 2021-11-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConsoleTrackerApp', '0003_machine_ip_squashed_0006_auto_20211119_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1', unique=True),
        ),
    ]