from django.contrib import admin
from .models import Product, Category, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
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
        'product_count',
    )

    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Number of Products'


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'rating',
        'created_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
