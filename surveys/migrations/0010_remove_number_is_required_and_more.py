# Generated by Django 5.0.1 on 2024-02-12 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0009_alter_phonenumber_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='is_required',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='is_required',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='is_visible',
        ),
        migrations.AddField(
            model_name='choices',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dropdown',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='longtext',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='number',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.toolssettings'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.toolssettings'),
        ),
        migrations.AddField(
            model_name='picturechoice',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='redirectwithurl',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='shorttext',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='toolssettings',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='yesno',
            name='label',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]