# Generated by Django 5.0.1 on 2024-03-20 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0081_alter_emailverification_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 12, 20, 26, 393354, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 12, 5, 26, 393354, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='expires_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 12, 20, 26, 393354, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 11, 55, 56, 393354, tzinfo=datetime.timezone.utc)),
        ),
    ]
