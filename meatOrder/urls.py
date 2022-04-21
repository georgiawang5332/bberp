from django.urls import path
from . import views

app_name = "meatOrder"

urlpatterns = [
    # path('searchOrder/', views.searchOrder, name="searchOrder"),
    path('listOrder/', views.listOrder, name="listOrder"),

]
