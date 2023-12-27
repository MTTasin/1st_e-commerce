from django.contrib import admin
from .models import product_table

# Register your models here.
class product_tableAdmin(admin.ModelAdmin):
    list_display = ('product_name','description','price','photo','category')
    
admin.site.register(product_table)
