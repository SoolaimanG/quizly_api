# Generated by Django 5.0.1 on 2024-02-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0008_endscreen_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='country_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='number_domain',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
