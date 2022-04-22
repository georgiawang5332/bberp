from django.db.models import Q
from django.shortcuts import render
from .filters import *


# Create your views here.
def listOrder(request):
    q_list = MeatOrder.objects.all()

    # order_number = request.GET["order_number"]
    # product_name = request.GET['product_name']
    # quantity = request.GET['quantity']
    # supplier_name = request.GET['supplier_name']
    # procurement_staff = request.GET['procurement_staff']
    # add_date = request.GET['add_date']
    # mod_date = request.GET['mod_date']
    # if order_number is not None:
    #     data = MeatOrder.objects.filter(
    #         order_number__icontains=order_number,
    #         # product_name__meatName__icontains=product_name,
    #         # quantity__icontains=quantity,
    #         # supplier_name__supplier_name__icontains=supplier_name,
    #         # procurement_staff__icontains=procurement_staff,
    #         # add_date__icontains=add_date,
    #         # mod_date__icontains=mod_date
    #     )

    # if order_number in request.POST:
    #     data = q_list.filter(
    #         Q(order_number__icontains=order_number)
    #     )

    q = request.GET.get("q")
    q_list = MeatOrder.objects.all()  # .filter(product_name__icontains=form['product_name'].value(), supplier_name__icontains=form['supplier_name'].value())
    if q:
        data = q_list.filter(
            Q(order_number__icontains=q) |
            Q(product_name__meatName__icontains=q) |
            Q(quantity__icontains=q) |
            Q(supplier_name__supplier_name__icontains=q) |
            Q(procurement_staff__icontains=q)
        ).distinct()  # .order_by('-mod_date')
    else:
        data = MeatOrder.objects.all()  # .order_by('-mod_date')
    context = {
        'data': data,
    }
    return render(request, 'meatOrder/index.html', context)
# 解答參考: https://stackoverflow.com/questions/66076215/related-field-got-invalid-lookup-icontains-django
