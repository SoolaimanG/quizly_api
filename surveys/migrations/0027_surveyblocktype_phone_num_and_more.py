# Generated by Django 5.0.1 on 2024-02-27 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0026_remove_surveyblocktype_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyblocktype',
            name='phone_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.phonenumber'),
        ),
        migrations.AlterField(
            model_name='surveyblocktype',
            name='picture_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture_choice_block', to='surveys.picturechoice'),
        ),
    ]
