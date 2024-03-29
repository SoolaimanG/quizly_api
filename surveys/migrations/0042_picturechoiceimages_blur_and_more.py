# Generated by Django 5.0.1 on 2024-03-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0041_picturechoiceimages_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturechoiceimages',
            name='blur',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picturechoiceimages',
            name='brightness',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picturechoiceimages',
            name='contrast',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picturechoiceimages',
            name='saturation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picturechoiceimages',
            name='x',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picturechoiceimages',
            name='y',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
