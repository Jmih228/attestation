# Generated by Django 5.0.7 on 2024-07-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='provider_debt',
            field=models.FloatField(blank=True, null=True, verbose_name='Задолженность перед поставщиком'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='provider_debt',
            field=models.FloatField(blank=True, null=True, verbose_name='Задолженность перед поставщиком'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='provider_debt',
            field=models.FloatField(blank=True, null=True, verbose_name='Задолженность перед поставщиком'),
        ),
    ]
