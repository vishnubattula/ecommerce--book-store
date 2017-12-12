from django.contrib import admin

# Register your models here.

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'sale_price','regular_price', 'stock','available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['sale_price','regular_price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)