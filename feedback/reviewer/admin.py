from django.contrib import admin

from reviewer.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_category', 'description', 'created_at', 'changed_at')
    list_filter = ('id', 'product_name', 'product_category', 'description', 'created_at', 'changed_at')
    search_fields = ('id', 'product_name', 'product_category', 'description', 'created_at', 'changed_at')
    fields = ('product_name', 'product_category', 'image', 'description')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'score', 'created_at', 'changed_at')
    list_filter = ('id', 'author', 'product', 'text', 'score', 'created_at', 'changed_at')
    search_fields = ('id', 'author', 'product', 'text', 'score', 'created_at', 'changed_at')
    fields = ('id', 'author', 'product', 'text', 'score')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
