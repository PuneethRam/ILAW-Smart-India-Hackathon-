# Generated by Django 3.2.6 on 2022-08-03 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_todo_field_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='field_name',
        ),
    ]