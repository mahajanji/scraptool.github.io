# Generated by Django 4.1 on 2022-09-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_actual_grade_actual_qualitys'),
    ]

    operations = [
        migrations.AddField(
            model_name='actual',
            name='recovery',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='actual',
            name='typeo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='actualmetal',
            name='po_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
