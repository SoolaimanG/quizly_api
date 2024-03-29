# Generated by Django 5.0.1 on 2024-03-20 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0084_alter_emailverification_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 20, 20, 12, 609227, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 20, 5, 12, 609227, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='featurewaitlist',
            name='feature_name',
            field=models.CharField(choices=[('IMAGE_FILTER', 'IMAGE_FILTER'), ('AI_HELP', 'AI_HELP'), ('QuestionGroup', 'QuestionGroup'), ('Time', 'Time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='expires_by',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 20, 20, 12, 608230, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forgetpassword',
            name='next_request',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 20, 19, 55, 42, 608230, tzinfo=datetime.timezone.utc)),
        ),
    ]
