# Generated by Django 5.0.4 on 2024-05-03 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('manufacture_year', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('wheels_number', models.IntegerField(blank=True, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.brand')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.color')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.type')),
            ],
        ),
    ]
