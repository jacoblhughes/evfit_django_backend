# Generated by Django 3.0.2 on 2020-01-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0010_remove_habit_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='slug',
            field=models.CharField(default='', max_length=255),
        ),
    ]
