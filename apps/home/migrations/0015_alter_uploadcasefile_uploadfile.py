# Generated by Django 4.0.5 on 2022-08-14 18:49

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_uploadcasefile_file_descripion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcasefile',
            name='uploadfile',
            field=models.FileField(blank=True, null=True, upload_to=apps.home.models.upload_handler),
        ),
    ]