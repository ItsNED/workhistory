# Generated by Django 2.0.9 on 2018-11-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20181113_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(blank=True, choices=[('ios', 'iOS'), ('aos', 'AOS')], max_length=30),
        ),
        migrations.AlterField(
            model_name='device',
            name='os_version',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]
