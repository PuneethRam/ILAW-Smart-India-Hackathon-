# Generated by Django 4.0.5 on 2022-08-20 06:33

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_case_similarcases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='similarcases',
            field=jsonfield.fields.JSONField(),
        ),
    ]
