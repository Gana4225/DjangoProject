# Generated by Django 5.1.4 on 2024-12-19 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('rn', models.CharField(max_length=250)),
                ('marks', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=15)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gana.branch')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gana.reg')),
            ],
        ),
    ]
