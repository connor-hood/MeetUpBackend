from django.contrib import admin
from .models import Category, Company, Comment, Product, ProductSite, ProductSize


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )


# Register your models here.
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(ProductSite)
admin.site.register(ProductSize)

# this changes the yellow text in admin
admin.site.site_header = "Product Review Admin"

# if we want to remove group model from Admin site:
# import Group from django.contrib.auth.models
# admin.site.unregister(Group)
