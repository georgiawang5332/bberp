from django.db.models import Q
from django.shortcuts import render
from .filters import *


# Create your views here.
def listOrder(request):
    q_list = MeatOrder.objects.all()
    q = request.GET.get("q")
    if q:
        data = q_list.filter(
            Q(order_number__icontains=q) |
            # Q(product_name__icontains=q) |
            Q(quantity__icontains=q) |
            # Q(supplier_name__icontains=q) |
            Q(procurement_staff__icontains=q)
        ).distinct()#.order_by('-mod_date')
    else:
        data = MeatOrder.objects.all()#.order_by('-mod_date')
    context = {
        'data': data,
    }
    return render(request, 'meatOrder/index.html', context)
