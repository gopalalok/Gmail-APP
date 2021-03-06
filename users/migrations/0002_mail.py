# Generated by Django 3.1.4 on 2021-02-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromemail', models.EmailField(max_length=254)),
                ('toemail', models.EmailField(max_length=254)),
                ('subject', models.TextField(blank=True, default='')),
                ('message', models.TextField(blank=True, default='')),
            ],
        ),
    ]
