# Generated by Django 4.0.6 on 2022-08-02 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shosho', '0009_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
