from .models import *
# import django_filters


# class meatOrderFilters(django_filters.FilterSet):
#     class Meat:
#         model = MeatOrder
#         fields = '__all__'

#
# class meatOrderFilters(django_filters.FilterSet):
#     # CHOICES = (
#     #     ('ascending', 'Ascending'),
#     #     ('descending', 'Descending')
#     # )
#     # ordering = django_filters.ChoiceFilter(label='Ordering', choices='CHOICES', method='filter_by_order')
#
#     class Meat:
#         model = MeatOrder
#         fields = {
#             'product_name': ['icontains', ],
#             'procurement_staff': ['icontains', ],
#         }

    # def filter_by_order(self, queryset, name, value):
    #     expression = 'created' if value == 'ascending' else 'created'
    #     return queryset.order_by(expression)
