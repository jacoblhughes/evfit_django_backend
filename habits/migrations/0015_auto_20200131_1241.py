# Generated by Django 3.0.2 on 2020-01-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0014_auto_20200130_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]