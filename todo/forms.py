from django.forms import ModelForm
from .models import car_info
from django import forms


class forme(ModelForm):
    class Meta:

        #Affect the model "car_info"
        model=car_info
        fields=['brand', 'consommation']
        queryset=car_info.objects.all()










