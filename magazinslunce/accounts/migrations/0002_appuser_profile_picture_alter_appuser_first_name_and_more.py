# Generated by Django 4.1.3 on 2022-11-24 16:50

import django.core.validators
from django.db import migrations, models
import magazinslunce.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pictures', validators=[magazinslunce.common.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), magazinslunce.common.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), magazinslunce.common.validators.validate_only_letters]),
        ),
    ]