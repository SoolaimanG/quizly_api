# Generated by Django 5.0.1 on 2024-02-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0029_phonenumbers_remove_yesno_label_yesno_allow_reselect_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyblocktype',
            name='index',
            field=models.PositiveIntegerField(default=1),
        ),
    ]