# Generated by Django 4.0.5 on 2022-08-20 06:45

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_case_similarcases'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='relevant_statues',
            field=jsonfield.fields.JSONField(default='default'),
            preserve_default=False,
        ),
    ]
