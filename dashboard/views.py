from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    template_name = 'dashboard/index.html'

    context = {

    }

    return render(request, template_name, context)
