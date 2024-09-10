from django.contrib import admin
from .models import About, Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
