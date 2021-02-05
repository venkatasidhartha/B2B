from django.shortcuts import render,redirect
from B2B_app.views import key_array
from B2B_cart.views import order
from django.http import HttpResponse
from .models import Order_model,Customer_model


#start editing to upload
# Create your views here.
def orderDisplay(request):
    if len(key_array) != 0:
        if request.method == 'POST':
            return HttpResponse('<h1>order placed </h1>')
        for i in order:
            store_order = Order_model.objects.create(username=Customer_model.objects.create(user=i["user"]),orderItem=i["item"],orderQuantity=i["quantity"])
            store_order.save()
        return render(request,'order.html',{'datas':order})
    else:
        return redirect("/")