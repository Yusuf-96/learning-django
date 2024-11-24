import uuid
from django.db import models


class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=50)
    stock = models.IntegerField(default=1)
    descriptions = models.TextField()
    price = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PRODUCTS"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["product_id", "product_name", "price"])]

    def __str__(self) -> str:
        return f"{self.price}"





