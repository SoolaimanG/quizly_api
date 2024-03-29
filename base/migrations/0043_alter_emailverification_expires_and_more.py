# Generated by Django 5.0.1 on 2024-02-13 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_emailverification_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 3, 31, 3, 348351, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 3, 16, 3, 348351, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='expires_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 3, 31, 3, 348351, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 3, 6, 33, 348351, tzinfo=datetime.timezone.utc)),
        ),
    ]
