# Generated by Django 5.0.1 on 2024-02-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_remove_userreponse_survey_userreponse_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomescreen',
            name='have_continue_button',
            field=models.BooleanField(default=True),
        ),
    ]
