# Generated by Django 2.1.7 on 2019-03-27 20:16

from django.db import migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190327_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=django_unixdatetimefield.fields.UnixDateTimeField(),
        ),
    ]