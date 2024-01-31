# Generated by Django 4.2.3 on 2023-07-13 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_attempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
        migrations.AddField(
            model_name='todo',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
