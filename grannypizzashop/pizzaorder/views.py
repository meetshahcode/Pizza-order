from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzas
from django.forms import formset_factory
from .models import Pizza

def edit_order(request,pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    notes = ""
    if request.method == "POST":
        filled_form = PizzaForm(request.POST,instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            notes = "order has Updated"
    return render(request, 'pizza/edit_order.html' ,{'pizzaform':form,'pizza':pizza,'notes':notes})

def home(request):
    return render(request,'pizza/home.html')

def order(request):
    multiple_pizzas_form = MultiplePizzas()
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        # form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            created_form = form.save()
            created_form_id = created_form.id
            note = 'Thanks for ordering!\nYour '+str(form.cleaned_data['size'])+' '+form.cleaned_data['topping1'] + ' and '+ form.cleaned_data['topping2']+ ' pizza is on the way.'
            form = PizzaForm()
        else:
            created_form_id = None
            note = 'Pizza order is not completed.\n'
        return render(request,'pizza/order.html',{"Pizzaform":form,"notes":note,"multiple_form":multiple_pizzas_form, 'created_form_id':created_form_id})
    else:
        Pizzaform = PizzaForm()
        return render(request,'pizza/order.html',{"Pizzaform":Pizzaform,"multiple_form":multiple_pizzas_form})

def Pizzas(request):
    numbers_pizzas = 2
    filed_multiple_pizza_form = MultiplePizzas(request.POST)
    if filed_multiple_pizza_form.is_valid():
        numbers_pizzas = filed_multiple_pizza_form.cleaned_data["numbers"]

    Pizzaformset = formset_factory(PizzaForm,extra = numbers_pizzas)
    formset = Pizzaformset()
    
    if request.method == 'POST':
        filledformset = Pizzaformset(request.POST)
        if filledformset.is_valid() :
            for form in filledformset:
                form.save()
            note = 'order was created.'
        else:
            note = 'order was not created.\n please try again.'
        return render(request,'pizza/pizzas.html',{'note':note,'formset':formset})
    else:
        return render(request,'pizza/pizzas.html',{'note':note,'formset':formset})