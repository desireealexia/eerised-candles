from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'stock',
        'image',
        'created_at',
        'updated_at'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'parent_category'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)