# Generated by Django 3.0.2 on 2020-02-06 04:17

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200205_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentprofile',
            name='program',
            field=models.FileField(blank=True, default='efportal/user_programs/welcome.xlsx', null=True, upload_to=accounts.models.upload_to),
        ),
    ]
