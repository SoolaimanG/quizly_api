# Generated by Django 5.0.1 on 2024-02-27 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0025_phonenumbercountries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyblocktype',
            name='phone_number',
        ),
    ]
