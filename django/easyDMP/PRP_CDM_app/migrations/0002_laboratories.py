# Generated by Django 5.0.6 on 2024-07-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRP_CDM_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('id_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'laboratories',
            },
        ),
    ]
