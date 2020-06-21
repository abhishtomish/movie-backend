from django.contrib import admin
from .models import *

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    list_filter = ['is_published']
    search_fields = ['title', 'is_published']

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)