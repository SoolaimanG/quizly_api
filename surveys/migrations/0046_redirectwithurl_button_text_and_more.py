# Generated by Django 5.0.1 on 2024-03-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0045_rename_label_redirectwithurl_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirectwithurl',
            name='button_text',
            field=models.CharField(default='Click here if you are not redirected.', max_length=500),
        ),
        migrations.AlterField(
            model_name='redirectwithurl',
            name='message',
            field=models.TextField(blank=True, default='Redirect to url', max_length=1000, null=True),
        ),
    ]