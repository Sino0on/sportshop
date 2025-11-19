from django.contrib import admin
from .models import *


class ImagesInline(admin.StackedInline):
    model = ProductImage
    extra = 1  # Количество пустых строк для добавления новых реквизитов
    fields = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]

# admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Category)
