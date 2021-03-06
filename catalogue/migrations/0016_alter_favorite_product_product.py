# Generated by Django 3.2.5 on 2021-08-19 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20210817_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite_product',
            name='product',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='search_product',
                to='catalogue.product'),
        ),
    ]
