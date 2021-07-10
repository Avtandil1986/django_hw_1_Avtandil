from django.contrib import admin
from Category.models import Category
from Category.models import Product
from Category.models import Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    search_fields = ['title', 'description']
    list_display = 'id title category price'.split()
    list_filter = 'category'.split()


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
