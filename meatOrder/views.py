from django.db.models import Q
from django.shortcuts import render
from .filters import *


# Create your views here.
def listOrder(request):
    # q = request.GET.get('q')
    # if q is not None:
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # data = MeatOrder.objects.filter(order_number__icontains=q)
        mult_data = Q(Q(product_name__icontains=q) | Q(quantity__icontains=q) | Q(supplier_name__icontains=q))
        data = MeatOrder.objects.filter(mult_data).distinct().order_by('-mod_date')
    else:
        data = MeatOrder.objects.all().order_by('-mod_date')

    context = {
        'data': data,
    }
    return render(request, 'meatOrder/index.html', context)
