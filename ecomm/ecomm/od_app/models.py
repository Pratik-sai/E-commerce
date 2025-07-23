from django.db import models

# Create your models here.

class Order(models.Model):
    cust_id = models.IntegerField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100)
    class Meta:
        db_table = 'orders'

class Cart(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'carts'




