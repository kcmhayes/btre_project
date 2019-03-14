from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    #fields that are displayed on the listings page table
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')

    #fields that will link
    list_display_links = ('id', 'title')

    #include filters
    list_filter = ('realtor',)

    #change publish field from the table
    list_editable = ('is_published',)

    #fields that can be used to filter database
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

    #number of listings to display before creating pagination
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
