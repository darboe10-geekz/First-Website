from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name', 'email')
    list_per_page = 10
    list_max_show_all = 100
