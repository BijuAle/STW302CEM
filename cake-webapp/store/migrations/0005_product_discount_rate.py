# Generated by Django 2.2.5 on 2019-10-23 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_shoppingcart_shoppingcartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_rate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
