# Generated by Django 4.1 on 2022-09-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_qualitymetal_weightage'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualmetal',
            name='actual_value',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='actualmetal',
            name='weightage',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
