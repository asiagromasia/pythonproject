from django import forms
from .models import Meeting,Minutes,Event,Resource

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

# from .models import Product, ProductType, Review

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields='__all__'