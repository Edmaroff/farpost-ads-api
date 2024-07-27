from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'farpost_id', 'author', 'views_count', 'position']
    list_filter = ['author']
    search_fields = ['title', 'author']
    ordering = ['position']
