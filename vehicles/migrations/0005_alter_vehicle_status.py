# Generated by Django 5.0.4 on 2024-05-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_alter_brand_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('ER', 'Em Revisão'), ('D', 'Disponível'), ('I', 'Indisponível')], max_length=2, null=True, verbose_name='Status'),
        ),
    ]