from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'updated_at', 'created_at',)
    list_filter = ('status',)
    search_fields = ('title', 'body',)
