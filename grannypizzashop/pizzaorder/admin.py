from django.contrib import admin
from .models import Pizza,Size
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id','topping1','topping2','size')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    '''Admin View for Size'''

    list_display = ('title',)