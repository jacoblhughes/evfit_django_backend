# Generated by Django 3.0.2 on 2020-02-10 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20200209_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rmbacksquatrecord',
            old_name='rmbackquat_user',
            new_name='rmbacksquat_user',
        ),
    ]