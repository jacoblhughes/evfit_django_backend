# Generated by Django 3.0.2 on 2020-02-10 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracking', '0002_auto_20200207_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightmeasurement',
            name='weight_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weightmeasurements', to='tracking.WeightRecord'),
        ),
        migrations.CreateModel(
            name='RMBackSquatRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('rmbackquat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RMBackSquatMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmbackquat', models.FloatField()),
                ('unit', models.CharField(default='lb', max_length=10)),
                ('created', models.DateField()),
                ('rmbackquat_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rmbackquatmeasurements', to='tracking.RMBackSquatRecord')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]