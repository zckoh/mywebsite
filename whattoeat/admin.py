from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','no_of_visits','date_added')
    list_filter = ['date_added']
    search_fields = ['name']

admin.site.register(Restaurant, RestaurantAdmin)
