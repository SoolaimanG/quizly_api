# Generated by Django 5.0.1 on 2024-02-23 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0020_surveys_number_of_submissions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveys',
            name='number_of_submissions',
        ),
    ]
