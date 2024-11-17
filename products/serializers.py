from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def create(self, validated_data):
        # product = Products.object.create(validated_data)
        # product = Products()
        # product.product_name= validated_data.get('product_name')
        # product.descriptions = validated_data.get('product_name')
        # product.save()

        return Products.object.create(validated_data)
    
    def update(self, instance, validated_data):
        pass

