# Generated by Django 5.0.1 on 2024-03-12 16:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0035_alter_date_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoicesOptions',
            fields=[
                ('option', models.CharField(max_length=1000)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.choices')),
            ],
        ),
    ]
