from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'image_show') 
    list_display_links = ('id', 'name')
    list_editable = ('price', )

    def image_show(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='60' />")
        return None
    
    image_show.__name__ = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category') 
    list_display_links = ('id', 'category')
