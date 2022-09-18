from django.contrib import admin
from products.models import Products

# Register your models here.

# admin.site.register(Products)

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "description", "is_active", "creation_date", "stock", "image"]
