# Generated by Django 2.0.9 on 2018-11-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceAdId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adid', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=30)),
                ('os_version', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deviceadid',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devices.Devices'),
        ),
    ]
