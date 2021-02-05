from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Food_items
from .serializers import FoodSerializer, OrderSerializer
import requests
from rest_framework.permissions import IsAuthenticated
from B2B_order.models import Order_model

# Create your views here.


class FoodViewset(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        food = Food_items.objects.all()
        return food

class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer


    def get_queryset(self):
        order = Order_model.objects.all()
        return order


key_array = []
user = []

def dashboard(request):

    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user.append(username)
            url = "http://127.0.0.1:8000/api/food/"
            payload = {}
            token_access = Token(username,password)
            headers = {
                        'Authorization': f'Bearer {token_access}'
                    }
            response = requests.request("GET", url, headers=headers, data=payload).json()
            key_array.append({"access":token_access})

            return redirect("/cart")
        else:
            return render(request, 'login.html')
    except:
        return render(request,'login.html')


def Token(username, password):
    payload = f'username={username}&password={password}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    Refresh = requests.request("POST", "http://127.0.0.1:8000/api/token/", headers=headers, data=payload).json()
    return Refresh_Token(Refresh["refresh"])

def Refresh_Token(refresh):
    url = "http://127.0.0.1:8000/api/token/refresh/"
    payload = f'refresh={refresh}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return response["access"]