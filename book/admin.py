from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'year', 'review')
	search_fields = ('title', 'author', 'year', 'review', 'average')