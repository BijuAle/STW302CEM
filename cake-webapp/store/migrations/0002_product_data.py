from datetime import timedelta
from django.utils import timezone
from django.db import migrations


def create_sample_product_data(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    Product(
        id=1, name='Florida Cake',
        description='Spongy apple cider base with fresh seasonal chopped fruits for topping. Vanilla sponge layered with flavored cream and filled with fresh fruits, kiwi & blueberry filling. Its topped and decorated with fruits + blueberry filling and decorated with roasted almonds on the sides (florida flavor)',
        price=1.00,
        photo='products/florida.jpg',
    ).save()
    Product(
        id=2, name='Black Forest',
        description='The classic black forest cake. Black Forest gâteau or Black Forest cake is a chocolate sponge cake with a rich cherry filling based on the German dessert Schwarzwälder Kirschtorte, literally "Black Forest Cherry-torte". Typically, Black Forest gateau consists of several layers of chocolate sponge cake sandwiched with whipped cream and cherries.',
        price=2.00,
        photo='products/cake3.jpg'
    ).save()
    Product(
        id=3, name='White Forest)',
        price=3.00,
        description='The classic white forest cake. It is made of layers of chocolate cake soaked in some kind of Kirsch or cherry based syrup layered with cherries and cream and frosted with more cream and covered in chocolate decorations. Every black forest cake is more or less made of these components with some innovation or creativity thrown in.',
        photo='products/lemon.jpg'
    ).save()
    Product(
        id=4, name='Chocolate cake',
        price=3.00,
        description='The classic chocolate cake. This chocolate cake recipe is similar to my Yellow Cake with Chocolate Frosting in that it’s a basic recipe that everyone needs in their collection.  If you are looking for something a little more “fancy,” check out my popular German Chocolate Cake or Coconut Cake with Pineapple Filling.',
        photo='products/torte.jpg'
    ).save()


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_product_data),
    ]
