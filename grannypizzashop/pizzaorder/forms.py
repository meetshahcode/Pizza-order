from cProfile import label
from dataclasses import fields
from django import forms
from .models import Pizza
# class PizzaForm(forms.Form):
#     Size_choice = [
#         ('Small','Small'),
#         ('Medium','Medium'),
#         ('Large','Large'),
#     ]
#     topping1 = forms.CharField(label="topping1",max_length=100)
#     topping2 = forms.CharField(label="topping2",max_length=100)
#     size = forms.ChoiceField(label="size",choices=Size_choice)

class PizzaForm(forms.ModelForm):
    """PizzaForm definition."""
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {
            'topping1':'Topping 1',
            'topping2':'Topping 2',
            'size' : 'Size'
        }
        

