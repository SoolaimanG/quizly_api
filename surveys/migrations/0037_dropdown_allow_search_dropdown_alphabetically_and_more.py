# Generated by Django 5.0.1 on 2024-03-14 14:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0036_choicesoptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropdown',
            name='allow_search',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dropdown',
            name='alphabetically',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dropdown',
            name='multiple_selection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dropdownopions',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dropdownopions',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
