from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Create your views here.
from django.http import HttpResponse


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        desc = request.POST.get('desc', "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', "")
        email = request.POST.get('email', "")
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    # this product is in the form of a list
    return render(request, 'shop/productview.html', {'myproduct': product[0]})


def checkout(request):
    if request.method == 'POST':
        itemJson = request.POST.get('itemsJson', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address1', "") + " " + request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        phone = request.POST.get('phone', "")
        zip_code = request.POST.get('zipcode', "")
        order = Order(items_json=itemJson, name=name, email=email, address=address, city=city, state=state,
                      zipcode=zip_code,
                      mobile_no=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed.")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
