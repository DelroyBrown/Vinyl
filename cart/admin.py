from django.contrib import admin
from .models import (Product,
                     OrderItem,
                     Order,
                     FormatVariation,
                     Address,
                     Payment,
                     Genre)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['artist_name', 'primary_genre']
    list_display = ['artist_name', 'album_title', 'spotify_link', 'price', 'primary_genre', 'stock', 'active']
    list_editable = ['stock', 'active', 'price', 'spotify_link']
    list_filter = ['primary_genre']
    prepopulated_fields = {"slug": ("album_title", "artist_name")}

    class Meta:
        model = Product


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'street_address',
        'town_or_city',
        'postcode',
        'county',
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre)
admin.site.register(FormatVariation)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Payment)
admin.site.register(Payment)
admin.site.register(Address, AddressAdmin)
