# Generated by Django 2.2.5 on 2019-10-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_discount_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='DISCOUNT_RATE',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
