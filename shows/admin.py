from django.contrib import admin
from .models import Category, Dresses, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


@admin.register(Dresses)
class DressesAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "dresses",
        "name",
        "image",
        "price",
        "discount",
        "discount_price",
    ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]
