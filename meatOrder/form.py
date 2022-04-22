from django.forms import ModelForm

from .models import MeatOrder

class SearchForm(ModelForm):
    class Meta:
        model = MeatOrder
        fields = '__all__'
