# Generated by Django 5.0.1 on 2024-02-27 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_alter_emailverification_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 20, 19, 36, 986968, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 20, 4, 36, 986968, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='expires_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 20, 19, 36, 986968, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 19, 55, 6, 986968, tzinfo=datetime.timezone.utc)),
        ),
    ]
