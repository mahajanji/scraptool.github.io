# Generated by Django 4.1 on 2022-09-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_actual_recovery_actual_typeo_actualmetal_po_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeNewValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='actualmetal',
            name='po_number',
        ),
        migrations.AddField(
            model_name='actual',
            name='po_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]