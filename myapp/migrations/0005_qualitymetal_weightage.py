# Generated by Django 4.1 on 2022-09-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_actual_remove_grademetal_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualitymetal',
            name='weightage',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]