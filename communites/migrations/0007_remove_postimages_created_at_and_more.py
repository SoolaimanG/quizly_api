# Generated by Django 5.0.1 on 2024-01-26 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communites', '0006_remove_community_posts_posts_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimages',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='postimages',
            name='updated_at',
        ),
    ]
