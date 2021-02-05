from django.db import models

# Create your models here.


class Customer_model(models.Model):
    user = models.CharField(max_length=100)


class Order_model(models.Model):
    username = models.ForeignKey(Customer_model,on_delete=models.CASCADE)
    orderItem = models.CharField(max_length=100)
    orderQuantity = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
