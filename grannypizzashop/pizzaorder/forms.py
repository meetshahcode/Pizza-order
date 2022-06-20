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
    # image = forms.ImageField()
    # email = forms.EmailField()
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {
            'topping1':'Topping 1',
            'topping2':'Topping 2'
        }
        widgets = {
            # 'topping1': forms.Textarea,
            # 'topping2':forms.PasswordInput
            #'size':forms.CheckboxSelectMultiple
            #'size':forms.CheckboxInput
            #'size':forms.RadioSelect
        }

class MultiplePizzas(forms.Form):
    """MultiplePizzas definition."""
    numbers = forms.IntegerField(min_value=2,max_value=5)
    # TODO: Define form fields here

