# Generated by Django 5.0.1 on 2024-02-25 14:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0022_remove_surveys_time_to_complete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endscreen',
            name='have_button',
        ),
        migrations.CreateModel(
            name='EndScreenSocialMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('social_media_link', models.URLField()),
                ('media_type', models.TextField(choices=[('instagram', 'INSTAGRAM'), ('facebook', 'FACEBOOK'), ('whatsapp', 'WHATSAPP'), ('twitter', 'TWITTER'), ('email', 'EMAIL'), ('tiktok', 'TIKTOK')], default='email', max_length=20)),
                ('end_screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.endscreen')),
            ],
        ),
    ]