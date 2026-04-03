from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_active')
    list_filter = ('is_active', 'published_date')
    search_fields = ('title', 'description', 'literature')
    ordering = ('-published_date',)
