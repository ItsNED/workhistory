# Generated by Django 2.0.9 on 2018-11-12 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oneonone', '0003_auto_20181112_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='events',
        ),
        migrations.RemoveField(
            model_name='app',
            name='os',
        ),
        migrations.RemoveField(
            model_name='app',
            name='tracking_url',
        ),
        migrations.AddField(
            model_name='content',
            name='events',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='os',
            field=models.CharField(choices=[('ios', 'iOS'), ('aos', 'AOS')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='store_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='tracking_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='adid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='devices.DeviceAdId'),
        ),
        migrations.AlterField(
            model_name='content',
            name='impression_id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='modified_url',
            field=models.TextField(blank=True),
        ),
    ]
