from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey('app.Category', default=None, on_delete=models.CASCADE)
    thumb = models.ImageField(default='default_product.png', null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'app_products'

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'app_categories'

class Feature(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_features'



class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title
    
    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total_price = models.IntegerField()

    def __str__(self):
        return 'Order # %s' % (str(self.id))

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amount, self.order.customer.username)

class View(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=3000, blank=True)

    def __str__(self):
        return self.user.username