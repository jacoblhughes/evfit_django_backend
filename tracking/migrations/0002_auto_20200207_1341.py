# Generated by Django 3.0.2 on 2020-02-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightmeasurement',
            name='created',
            field=models.DateField(),
        ),
    ]
