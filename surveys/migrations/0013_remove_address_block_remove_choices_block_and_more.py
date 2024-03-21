# Generated by Django 5.0.1 on 2024-02-13 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0012_alter_address_block_alter_choices_block_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='block',
        ),
        migrations.RemoveField(
            model_name='choices',
            name='block',
        ),
        migrations.RemoveField(
            model_name='date',
            name='block',
        ),
        migrations.RemoveField(
            model_name='dropdown',
            name='block',
        ),
        migrations.RemoveField(
            model_name='email',
            name='block',
        ),
        migrations.RemoveField(
            model_name='endscreen',
            name='block',
        ),
        migrations.RemoveField(
            model_name='longtext',
            name='block',
        ),
        migrations.RemoveField(
            model_name='number',
            name='block',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='block',
        ),
        migrations.RemoveField(
            model_name='picturechoice',
            name='block',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='block',
        ),
        migrations.RemoveField(
            model_name='redirectwithurl',
            name='block',
        ),
        migrations.RemoveField(
            model_name='shorttext',
            name='block',
        ),
        migrations.RemoveField(
            model_name='website',
            name='block',
        ),
        migrations.RemoveField(
            model_name='welcomescreen',
            name='block',
        ),
        migrations.RemoveField(
            model_name='yesno',
            name='block',
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_blocks', to='surveys.address'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='choices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices_blocks', to='surveys.choices'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='contact_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_info_blocks', to='surveys.contactinfo'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_blocks', to='surveys.date'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='dropdown',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dropdown_blocks', to='surveys.dropdown'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_blocks', to='surveys.email'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='end_screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_screen_blocks', to='surveys.endscreen'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='label',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='long_text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='long_text_blocks', to='surveys.longtext'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='number_blocks', to='surveys.number'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='phone_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_number_blocks', to='surveys.phonenumber'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='picture_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture_choice_blocks', to='surveys.picturechoice'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='ratings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_blocks', to='surveys.rating'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='redirect_with_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redirect_with_url_blocks', to='surveys.redirectwithurl'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='short_text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='short_text_blocks', to='surveys.shorttext'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='website_blocks', to='surveys.website'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='welcome_screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='welcome_screen_blocks', to='surveys.welcomescreen'),
        ),
        migrations.AddField(
            model_name='surveyblocktype',
            name='yes_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yes_no_blocks', to='surveys.yesno'),
        ),
        migrations.AlterField(
            model_name='surveyblocktype',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_blocks', to='surveys.surveys'),
        ),
    ]