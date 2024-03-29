# Generated by Django 5.0.1 on 2024-02-12 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0010_remove_number_is_required_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropdown',
            name='option',
        ),
        migrations.AlterField(
            model_name='userreponse',
            name='block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.surveyblocktype'),
        ),
        migrations.CreateModel(
            name='DropDownOpions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('drop_down', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.dropdown')),
            ],
        ),
    ]
