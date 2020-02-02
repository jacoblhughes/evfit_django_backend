# Generated by Django 3.0.2 on 2020-02-02 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0015_auto_20200131_1241'),
        ('accounts', '0015_auto_20200131_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='habits.Habit'),
        ),
    ]
