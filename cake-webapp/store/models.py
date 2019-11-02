
from django.utils import timezone
from django.db import models
from django.conf import settings

OCCASIONS = (
    ('B', 'Birthday'),
    ('A', 'Anniversary'),
    ('W', 'Wedding'),
    ('G', 'General')
)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    occasion = models.CharField(choices=OCCASIONS, max_length=2, default='G')
    price = models.FloatField()
    discount_rate = models.FloatField(null=False, blank=True, default=0)
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True,default=None, upload_to='products')

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_price(self):
        return self.price

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.discount_rate)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)

    def __str__(self):
        return self.name

class OrderItem (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.qty} of {self.item.name}"

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
