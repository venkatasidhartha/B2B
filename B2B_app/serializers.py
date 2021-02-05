from rest_framework import serializers
from .models import Food_items
from B2B_order.models import Order_model

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_items
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_model
        fields = ['username','orderItem','orderQuantity','time']
        depth = 1
