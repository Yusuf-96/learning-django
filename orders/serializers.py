from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from .models import Order, OrderItem
from products.models import Products
from django.db import transaction

# How order Items/Product
"""
>> Get the product(getById)
>> Add product in orderItem
       - is that available in stock(5)
       - How many item (4)
       - deducting product stock
>> Order it.
"""


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = OrderItem
        fields = "__all__"

    def create(self, validated_data):
        product_id = validated_data.get("product_id", None)
        quantity = validated_data.get("quantity", None)

        if product_id is None:
            raise serializers.ValidationError(
                {"message": "Product Id is a required field"}
            )

        if quantity is None:
            raise serializers.ValidationError(
                {"message": "quantity is a required field"}
            )

        try:
            product = get_object_or_404(Products, product_id=product_id)

        except Http404:
            raise serializers.ValidationError(
                {"message": "Product not found", "status": status.HTTP_404_NOT_FOUND}
            )

        stock = product.stock

        if stock <= 0:
            raise serializers.ValidationError(
                {
                    "message": "Product is unavailable",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )

        if quantity > stock:
            raise serializers.ValidationError(
                {
                    "message": "Quantity  exceeds stock ",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )

        total_price = quantity * product.price

        with transaction.atomic():
            order_item = OrderItem.objects.create(
                quantity=quantity, total_item_price=total_price, products=product
            )

            Order.objects.create(order_item=order_item, total_price=total_price)

            product.stock -= quantity

            product.save()

            return order_item
