# Generated by Django 3.1.5 on 2021-07-02 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exerciselog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseinformation',
            name='exercise_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciseformation', to='exerciselog.exerciserecord'),
        ),
    ]
