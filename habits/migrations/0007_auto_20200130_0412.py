# Generated by Django 3.0.2 on 2020-01-30 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_remove_habit_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='description',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='members',
        ),
    ]
