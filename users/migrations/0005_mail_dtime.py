# Generated by Django 3.1.4 on 2021-02-17 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210217_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='dtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
