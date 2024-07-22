# serializers.py
from rest_framework import serializers
from .models import Orders, OrderProduct
from products.models import Product

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'order', 'product', 'quantity']

class OrdersSerializer(serializers.ModelSerializer):
    #order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['id', 'user', 'isActive', 'orderDate']
