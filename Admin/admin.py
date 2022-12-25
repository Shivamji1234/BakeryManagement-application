from django.contrib import admin
from Admin.models import Items, Ingredients
from Customer.models import Customer, Order

# Register your models here.

admin.site.register(Items)
admin.site.register(Ingredients)
admin.site.register(Customer)
admin.site.register(Order)


