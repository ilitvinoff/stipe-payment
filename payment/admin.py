from django.contrib import admin

# Register your models here.
from payment.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name',)
