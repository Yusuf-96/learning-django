from django.db import models
from products.models import Products


class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    products = models.ForeignKey(
        Products, related_name="order_items", on_delete=models.CASCADE
    )
    total_item_price = models.DecimalField(decimal_places=2)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table ='ORDERITEMS'
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return f'{self.quantity}'


class Order(models.Model):
    order_item = models.ForeignKey(
        OrderItem,
        related_name="orders",
        on_delete=models.CASCADE,
        # on_delete=models.SET_NULL,
        # blank=True,
        # null=True,
    )
    total_price = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ORDERS'
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return f'{self.total_price}'
