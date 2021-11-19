# Generated by Django 3.2.8 on 2021-11-19 07:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('ConsoleTrackerApp', '0003_machine_ip'), ('ConsoleTrackerApp', '0004_user_user_uses_machine'), ('ConsoleTrackerApp', '0005_user_uses_machine_expired'), ('ConsoleTrackerApp', '0006_auto_20211119_0203')]

    dependencies = [
        ('ConsoleTrackerApp', '0002_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User_uses_machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConsoleTrackerApp.machine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConsoleTrackerApp.user')),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]