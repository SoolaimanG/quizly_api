# Generated by Django 5.0.1 on 2024-02-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_remove_surveyblocktype_number_address_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='endscreen',
            name='button_text',
            field=models.TextField(default='Button', max_length=50, null=True),
        ),
    ]
