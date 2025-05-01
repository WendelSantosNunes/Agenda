from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'created_date', 'show',
    ordering='id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', 'show'
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 
    ordering='id',