# Generated by Django 5.0.1 on 2024-02-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0024_remove_surveyblocktype_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberCountries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]