# Generated by Django 2.0.9 on 2018-11-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_auto_20181113_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(choices=[('ios', 'iOS'), ('aos', 'AOS')], max_length=30),
        ),
    ]
