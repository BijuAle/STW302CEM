from datetime import timedelta
from django.utils import timezone
from django.db import migrations

def create_sample_product_data(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    Product(
        id=1, name='Florida Cake', description='Spongy apple cider base with fresh seasonal chopped fruits for topping.', price=1.00,
        photo='products/mineralwater-strawberry.jpg',
    ).save()
    Product(
        id=2, name='Black Forest', description='The classic black forest cake.', price=2.00,
        photo='products/mineralwater-raspberry.jpg',
    ).save()
    Product(
        id=3, name='White Forest)', price=3.00,
        description='The classic white forest cake.',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/vitamin-a.jpg',
    ).save()
    Product(
        id=4, name='Chocolate cake', price=3.00,
        description='The classic chocolate cake.',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/vitamin-bcomplex.jpg',
    ).save()

class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_product_data),
    ]
