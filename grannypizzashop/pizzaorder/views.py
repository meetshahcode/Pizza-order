from django.shortcuts import render
from .forms import PizzaForm
def home(request):
    return render(request,'pizza/home.html')
def order(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            note = 'Thanks for ordering!\n Your '+form.cleaned_data['size']+' '+form.cleaned_data['topping1'] + ' and '+ form.cleaned_data['topping2']+ ' pizza is on the way.'
            Pizzaform = PizzaForm()
            return render(request,'pizza/order.html',{"Pizzaform":Pizzaform,"notes":note})
    else:
        Pizzaform = PizzaForm()
        return render(request,'pizza/order.html',{"Pizzaform":Pizzaform})

