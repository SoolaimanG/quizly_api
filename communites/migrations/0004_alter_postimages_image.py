# Generated by Django 5.0.1 on 2024-01-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communites', '0003_alter_community_display_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.URLField(),
        ),
    ]
