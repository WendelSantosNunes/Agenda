from django.contrib import admin
from contact.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'created_date',
    ordering='id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 1
