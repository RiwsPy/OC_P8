# Generated by Django 3.2.5 on 2021-08-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20210804_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='catalogue.Category', verbose_name='list of category'),
        ),
    ]
