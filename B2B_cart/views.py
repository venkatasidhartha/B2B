from django.shortcuts import render, redirect
from B2B_app.views import key_array,user
import requests
# Create your views here.
order = []
def cart(request):
    try:
        if len(key_array) != 0:
            url = "http://127.0.0.1:8000/api/food/"
            payload = {}
            token_access = key_array[-1]
            headers = {
                'Authorization': f'Bearer {token_access["access"]}'
            }
            response = requests.request("GET", url, headers=headers, data=payload).json()

            if request.method == 'POST':
                item = request.POST["item"]
                quantity = request.POST["quantity"]

                order.append({"item":item, "quantity":quantity,"user":user[-1]})
            print(request.user,order)

            return render(request, 'dashboard.html', {'datas': response})
    except:
        return redirect("/")

