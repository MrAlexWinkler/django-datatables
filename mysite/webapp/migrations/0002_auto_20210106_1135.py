# Generated by Django 3.1.3 on 2021-01-06 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='created',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='modified',
        ),
    ]