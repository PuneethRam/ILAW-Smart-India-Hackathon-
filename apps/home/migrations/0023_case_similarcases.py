# Generated by Django 4.0.5 on 2022-08-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_uploadcasefile_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='similarcases',
            field=models.CharField(default=False, max_length=10000),
        ),
    ]
