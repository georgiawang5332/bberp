from django.db.models import Q
from django.shortcuts import render
from .filters import *


# Create your views here.
def listOrder(request):
    # form = StoreSearchForm(request.POST or None)

    q_list = MeatOrder.objects.all()#.filter(product_name__icontains=form['product_name'].value(), supplier_name__icontains=form['supplier_name'].value())
    q = request.GET.get("q")
    getobject = request.GET['search']
    getcategory = request.GET['category']

    if q:
        data = q_list.filter(
            Q(order_number__icontains=q) |
            Q(product_name__meatName__icontains=q) |
            Q(quantity__icontains=q) |
            Q(supplier_name__supplier_name__icontains=q) |
            Q(procurement_staff__icontains=q)
        ).distinct()#.order_by('-mod_date')
    else:
        data = MeatOrder.objects.all()#.order_by('-mod_date')
    context = {
        'data': data,
    }
    return render(request, 'meatOrder/index.html', context)
# 解答參考: https://stackoverflow.com/questions/66076215/related-field-got-invalid-lookup-icontains-django
