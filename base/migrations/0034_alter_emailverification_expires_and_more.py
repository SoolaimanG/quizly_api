# Generated by Django 5.0.1 on 2024-02-10 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_emailverification_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 49, 52, 282843, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 34, 52, 282843, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='expires_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 49, 52, 282843, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 14, 25, 22, 282843, tzinfo=datetime.timezone.utc)),
        ),
    ]
