# Generated by Django 5.0.6 on 2024-07-15 12:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRP_CDM_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('uuid', models.CharField(default=uuid.UUID('78ac430f-d4b2-463d-bcfe-9cfa9df37fd1'), max_length=37, primary_key=True, serialize=False)),
                ('dmptitle', models.CharField(blank=True, max_length=50)),
                ('datausername', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=128)),
                ('affiliation', models.CharField(blank=True, max_length=128)),
                ('experimentabstract', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'administration',
            },
        ),
        migrations.CreateModel(
            name='lageSample',
            fields=[
                ('uuid', models.CharField(default=uuid.UUID('88018f81-ad16-4fb6-9fc6-64bfcfa3682f'), max_length=37, primary_key=True, serialize=False)),
                ('datausername', models.CharField(max_length=50)),
                ('sample_description', models.TextField(max_length=500)),
                ('type_of_sample', models.CharField(blank=True)),
                ('is_volume_in_uL', models.CharField(blank=True)),
                ('is_buffer_used', models.CharField(blank=True)),
                ('expected_date_of_delivery', models.DateField()),
                ('is_quality', models.CharField(blank=True)),
                ('sample_back', models.BooleanField()),
            ],
            options={
                'db_table': 'lagesample',
            },
        ),
        migrations.AlterField(
            model_name='customappmodel',
            name='datavarchar',
            field=models.CharField(default=uuid.UUID('27f65424-56c4-4ed5-a32e-0d3a1419c1b2'), max_length=255, primary_key=True, serialize=False),
        ),
    ]
